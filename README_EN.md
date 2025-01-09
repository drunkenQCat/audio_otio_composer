# Audio to DaVinci OTIO Generator  

This project aims to generate a DaVinci-compatible OpenTimelineIO (OTIO) file from a folder containing multiple WAV audio files.  

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

```python  
@click.option(
    "--path",
    "-p",
    default="test_data",
    help="Input data path, usually a folder containing audio files.",
)
@click.option("--output", "-o", help="Output filename for the generated OTIO timeline file.")
```  

---  

## Project Background  

This project is inspired by [IgorRidanovic/randomOTIO](https://github.com/IgorRidanovic/randomOTIO) and aims to simplify the process of generating OTIO files from audio files, providing a more efficient workflow for post-production teams.  

### Key Features:  
- **Automated Timeline Generation**: Automatically reads metadata from WAV audio files to create OTIO files with precise timecodes and audio ranges.  
- **Seamless DaVinci Integration**: The generated OTIO files can be directly imported into DaVinci, reducing manual adjustments.  
- **Comprehensive Metadata Parsing**: Supports WAV metadata, including time offsets, role names, and channel counts, and maps them to corresponding fields in the DaVinci timeline.  

---  

## Preparing Audio Data  

**Important Reminder:**  
Ensure the WAV audio files meet the following metadata requirements before using this tool; otherwise, the generated timeline may not work as expected.  

### Required Audio Metadata  
The tool depends on the following metadata to generate OTIO files:  
1. **Time Reference**  
    - Marks the start offset of the audio. Without this, all audio files will start at the zero point on the timeline, causing issues like vertical stacking of all audio clips.  

### Optional Audio Metadata  
1. **Artist Information (Role Name)**  
    - This will be mapped to the track name in the DaVinci timeline.  

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
