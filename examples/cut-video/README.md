# `cut-video` examples

Some examples, changing the `distance` parameter.

- `default.mkv`: The original file
- `result_negative.mp4`: `-d negative`
- `result_tiny.mp4`: Default cuts
- `result_small.mp4`: `-d small`
- `result_medium.mp4`: `-d medium`
- `result_large.mp4`: `-d large`

All these examples using defaults parameters to `threshold`, `silence-time`, `bitrate` and `codec`.

The `--preset` used is `ultrafast`

Example command:

```bash
vmh cut-video default.mkv result_large.mp4 -p ultrafast -d large
```
