from itertools import islice, pairwise
from os import getcwd
from pathlib import Path
from typing import Literal, cast
from xml.etree import ElementTree

from loguru import logger
from parsel.selector import Selector

from vmh.audio import detect_silences

xml_template = """ <entry producer="{}" in="00:00:{:.3f}" out="00:00:{:.3f}">
   <property name=:id">{}</property>
  </entry>
"""


def check_chain(
    filename: Path,
    input_file: Path,
    property: int | None = None,
) -> tuple[str, ...]:
    with open(input_file) as f:
        content = f.read()
        s = Selector(content)

        if property:
            el = s.xpath(
                f"""
    //chain[(
        (./property[(@name='resource' and ./text()='{str(filename)}')])
        and
        (./property[(@name='set.test_audio' and ./text()='{property}')])
    )]
""",
            )
        else:
            el = s.xpath(f'//chain/property[text() = "{str(filename)}"]/..')

        _chain = el.css('chain::attr("id")').get()
        _chain = cast(str, _chain)
        _id = el.css('property[name="kdenlive:id"]::text').get()
        _id = cast(str, _id)

        playlists = s.xpath(
            f'//playlist/entry[@producer="{_chain}"]/..',
        ).xpath('@id')

        logger.debug(f'Playlists: {filename}-{playlists}')
        playlist_id = playlists.get()
        playlist_id = cast(str, playlist_id)

        return _chain, _id, playlist_id


def kdenlive_xml(
    path: str,
    playlist_id: str,
    property_id: str,
    chain_id: str,
    cuts: list[float],
    output_path: str,
    *,
    overwrite: bool = False,
) -> str:
    tree = ElementTree.parse(path)
    root = tree.getroot()

    playlist = root.find(f'./playlist[@id="{playlist_id}"]')
    playlist = cast(ElementTree.Element, playlist)

    playlist.clear()
    playlist.attrib.update(id=playlist_id)

    for _in, _out in islice(pairwise(cuts), 1, None, 2):
        entry_attribs = {
            'producer': chain_id,
            'in': f'00:00:{_in:.3f}',
            'out': f'00:00:{_out:.3f}',
        }
        entry = ElementTree.SubElement(playlist, 'entry', attrib=entry_attribs)

        ElementTree.SubElement(
            entry,
            'property',
            attrib={'name': 'kdenlive:id'},
        ).text = property_id

    if overwrite:
        tree.write(path)
        return path

    tree.write(output_path)
    return output_path


def cut(
    audio_file: Path,
    video_file: Path,
    input_file: Path,
    output_path: Path,
    silence_time,
    threshold: int,
    force: bool,
    distance: Literal[
        'negative',
        'tiny',
        'small',
        'medium',
        'large',
        'huge',
    ] = 'tiny',
) -> Path:
    if audio_file != Path(getcwd()):  # Typer don't support Path | None
        times = detect_silences(
            str(audio_file),
            silence_time,
            threshold,
            distance,
            force=force,
        )
    else:
        times = detect_silences(
            str(video_file),
            silence_time,
            threshold,
            distance,
            force=force,
        )

    chain_id, file_id, playlist = check_chain(video_file, input_file, 0)

    _output_path: str = kdenlive_xml(
        str(input_file),
        playlist_id=playlist,
        property_id=file_id,
        chain_id=chain_id,
        cuts=times,
        output_path=str(output_path),
    )
    logger.info(f'Video playlist {playlist}')

    chain_id, file_id, playlist = check_chain(video_file, input_file, 1)
    kdenlive_xml(
        _output_path,
        playlist_id=playlist,
        chain_id=chain_id,
        property_id=file_id,
        cuts=times,
        output_path=_output_path,
    )
    logger.info(f'Audio playlist {playlist}')

    if audio_file != Path(getcwd()):  # Typer don't support Path | None
        chain_id, file_id, playlist = check_chain(audio_file, input_file)
        kdenlive_xml(
            _output_path,
            playlist_id=playlist,
            chain_id=chain_id,
            property_id=file_id,
            cuts=times,
            output_path=_output_path,
        )
        logger.info(f'Audio playlist {playlist}')

    return Path(_output_path).resolve()
