# Audio to DaVinci OTIO Generator

This project is designed to generate an OpenTimelineIO (OTIO) file compatible with DaVinci Resolve from a folder containing multiple WAV audio files.

## Installation

1. Install the package manager `uv`:

    ```bash
    pip install uv
    ```

2. Sync the virtual environment:

    ```bash
    uv sync
    ```

## Usage

Run the script with the following command:

```bash
uv run otio_generator.py
```

## Project Background

This project is inspired by [IgorRidanovic/randomOTIO](https://github.com/IgorRidanovic/randomOTIO), aiming to simplify the process of generating OTIO files from audio files, facilitating post-production in DaVinci Resolve.

## License

This project is licensed under the [MIT License](LICENSE). 