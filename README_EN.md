# Audio OTIO Generator (DaVinci Resolve / Premiere Pro)

This project generates a DaVinci Resolve and/or Premiere Pro-compatible OpenTimelineIO (OTIO) file from a folder containing multiple WAV audio files.

[中文说明](README.md)

---

## Installation

1. Install the package manager `uv`:

    ```bash
    pip install uv
    ```

2. Synchronize the virtual environment:

    ```bash
    uv sync
    ```

---

## Usage

Run the script with the following command:

```bash
uv run otio_generator.py
```

By default, the script reads files from the `test_data` folder. Optional parameters:

```bash
-p, --path           Input data path, usually a folder containing audio files (default: test_data)
-o, --output         Output filename (default: test_data, auto-appended with timestamp)
-f, --fps            Frame rate (default: 24.0)
-m, --metadata-mode  Metadata mode (default: mix)
                     mix      - Both Resolve + Premiere Pro metadata
                     resolve  - DaVinci Resolve metadata only
                     premiere - Premiere Pro metadata only
```

Examples:

```bash
# Generate a timeline compatible with both Resolve and Premiere Pro
uv run otio_generator.py -p /path/to/audio -o my_project -m mix

# Generate Premiere Pro format only
uv run otio_generator.py -p /path/to/audio -o my_project -m premiere
```

---

## Project Background

This project is inspired by [IgorRidanovic/randomOTIO](https://github.com/IgorRidanovic/randomOTIO) and aims to simplify the process of generating OTIO files from audio files, providing a more efficient workflow for post-production teams.

### Key Features:

- **Automated Timeline Generation**: Automatically reads metadata from WAV audio files to create OTIO files with precise timecodes and audio ranges.
- **Multi-Software Compatibility**:
  - **DaVinci Resolve**: Direct import with audio effects, channel mapping, and other metadata.
  - **Premiere Pro**: Supports PR-format track/clip effects (AudioFader, PanProcessor, etc.) and full `PremierePro_OTIO` metadata structure.
- **Smart Track Allocation**: Uses scanline algorithm to automatically arrange overlapping audio clips on separate tracks, grouped by character.
- **Comprehensive Metadata Parsing**: Supports WAV metadata including time offsets (`bext.time_reference`), character names (`info.artist`), and channel counts, mapping them to corresponding timeline fields.

---

## Preparing Audio Data

**Important Reminder:**
Ensure the WAV audio files meet the following metadata requirements before using this tool; otherwise, the generated timeline may not work as expected.

### Required Audio Metadata
The tool depends on the following metadata to generate OTIO files:
1. **Time Reference**
    - Marks the start offset of the audio. Without this, all audio files will start at the zero point on the timeline, causing issues like vertical stacking of all audio clips.

### Optional Audio Metadata
1. **Artist Information (Role/Character Name)**
    - This will be mapped to the track name in the timeline.
2. **Channel Count**
    - Used to auto-detect Mono/Stereo, affecting track and clip effect configuration.

---

## How to Generate Time Reference

If your WAV files lack the time reference metadata, you can manually add it. Below are the steps to generate time references in Reaper:

1. When batch exporting audio items:
    - **Uncheck**: `Preserve start offset` and `Preserve metadata`.
    - **Check**: `Add new metadata`.

2. The generated WAV files will automatically include the time offset in `bext.time reference`.

### Other Metadata Generation Methods
- Artist information and channel count can be manually added by editing the WAV file metadata as needed.

---

## License

This project is licensed under the [MIT License](LICENSE).
