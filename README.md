# img2webp

A Python script to convert images to WebP format while preserving original filenames.

## Features

- Converts images from multiple formats (JPG, PNG, BMP, GIF, TIFF) to WebP
- Preserves original filenames (only changes the extension)
- Supports transparency for PNG/GIF images
- Configurable output quality
- Batch processing of entire folders
- Option to overwrite existing files

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

**On Windows, if `pip` is not recognized, use:**
```bash
py -m pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python convert_to_webp.py <input_folder> <output_folder>
```

**On Windows, use `py` instead of `python`:**
```bash
py convert_to_webp.py <input_folder> <output_folder>
```

With custom quality setting (1-100):
```bash
python convert_to_webp.py <input_folder> <output_folder> 90
```

Overwrite existing .webp files:
```bash
python convert_to_webp.py <input_folder> <output_folder> 85 --overwrite
```

### Examples

Convert all images from "input" folder to "output" folder with default quality (85):
```bash
python convert_to_webp.py ./input ./output
```

Convert with high quality (95):
```bash
python convert_to_webp.py ./input ./output 95
```

Convert and overwrite existing .webp files in output folder:
```bash
python convert_to_webp.py ./input ./output 90 --overwrite
```

## Supported Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff, .tif)
- WebP (.webp)

## Output

The script will:
- Display the number of images found
- Show progress for each image conversion
- Provide a summary of conversions, skipped files, and errors
- Create .webp files in the specified output folder
- Automatically create the output folder if it doesn't exist

## Notes

- Original files are NOT deleted - they remain in the folder
- If a .webp file already exists, it will be skipped unless you use `--overwrite`
- Images with transparency (PNG/GIF) will maintain their transparency in WebP format
- Default quality setting is 85 (good balance between quality and file size)