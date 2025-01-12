from importlib import import_module
from pathlib import Path
from typing import TypeAlias

from pedalboard import Pedalboard
from pedalboard.io import AudioFile  # type: ignore

T_fx_chain: TypeAlias = dict[str, dict[str, float]]

fx_chain: T_fx_chain = {
    'NoiseGate': {
        'attack_ms': 100,
        'release_ms': 200,
        'threshold_db': -30,
        'ratio': 4,
    },
    'Compressor': {
        'attack_ms': 0,
        'release_ms': 250,
        'threshold_db': -33.5,
        'ratio': 2,
    },
    'Gain': {'gain_db': -12},
    'Limiter': {'release_ms': 0, 'threshold_db': -1},
}


def _get_board() -> Pedalboard:
    pedalboard = import_module('pedalboard')

    """
    NOTE: Not implemented yet
    from json import loads
    from vmh import settings
    if settings.eq_config_path.exists():
        effects: T_fx_chain = loads(settings.eq_config_path.read_text())
    else:
        effects = fx_chain
    """
    effects = fx_chain

    plugins = [getattr(pedalboard, effect)(**effects[effect]) for effect in effects]

    return Pedalboard(plugins)


def process_audio(
    input_file: str,
    output_file: str = 'output.wav',
    board: Pedalboard = _get_board(),
) -> Path:
    with AudioFile(input_file, 'r') as ifile:
        with AudioFile(
            output_file,
            'w',
            ifile.samplerate,
            ifile.num_channels,
        ) as ofile:
            while ifile.tell() < ifile.frames:
                chunk = ifile.read(ifile.samplerate)
                effected = board(chunk, ifile.samplerate, reset=False)
                ofile.write(effected)

    return Path(output_file)
