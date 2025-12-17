#!/usr/bin/env python3
"""
Convert all images in a folder to WebP format.
Preserves original filenames, only changing the extension to .webp
"""

import os
import sys
from pathlib import Path
from PIL import Image

# Supported image formats
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif', '.webp'}

def convert_to_webp(input_folder, output_folder, quality=85, overwrite=False):
    """
    Convert all images in a folder to WebP format.
    
    Args:
        input_folder: Path to the folder containing images
        output_folder: Path to the folder where converted images will be saved
        quality: Quality of the output WebP images (1-100, default: 85)
        overwrite: If True, overwrites existing .webp files
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    if not input_path.exists():
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return
    
    if not input_path.is_dir():
        print(f"Error: '{input_folder}' is not a directory.")
        return
    
    # Create output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"Output folder: {output_path.absolute()}")
    
    # Find all image files
    image_files = []
    for ext in SUPPORTED_FORMATS:
        image_files.extend(input_path.glob(f'*{ext}'))
        image_files.extend(input_path.glob(f'*{ext.upper()}'))
    
    if not image_files:
        print(f"No image files found in '{input_folder}'")
        return
    
    print(f"Found {len(image_files)} image(s) to convert")
    print(f"Output quality: {quality}")
    print("-" * 50)
    
    converted_count = 0
    skipped_count = 0
    error_count = 0
    
    for image_file in image_files:
        # Get the output filename (same name, .webp extension, in output folder)
        output_file = output_path / image_file.with_suffix('.webp').name
        
        # Skip if already a .webp file converting to itself
        if image_file == output_file:
            print(f"Skipping: {image_file.name} (already .webp)")
            skipped_count += 1
            continue
        
        # Check if output file already exists
        if output_file.exists() and not overwrite:
            print(f"Skipping: {image_file.name} (output already exists)")
            skipped_count += 1
            continue
        
        try:
            # Open and convert the image
            with Image.open(image_file) as img:
                # Convert RGBA to RGB if necessary (for formats that don't support transparency)
                if img.mode in ('RGBA', 'LA', 'P'):
                    # Keep transparency for WebP
                    img.save(output_file, 'WEBP', quality=quality, method=6)
                else:
                    img.save(output_file, 'WEBP', quality=quality)
            
            print(f"Converted: {image_file.name} -> {output_file.name}")
            converted_count += 1
            
        except Exception as e:
            print(f"Error converting {image_file.name}: {str(e)}")
            error_count += 1
    
    print("-" * 50)
    print(f"Conversion complete!")
    print(f"  Converted: {converted_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors: {error_count}")

def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python convert_to_webp.py <input_folder> <output_folder> [quality] [--overwrite]")
        print("  input_folder: Path to the folder containing images")
        print("  output_folder: Path to the folder where converted images will be saved")
        print("  quality: WebP quality (1-100, default: 85)")
        print("  --overwrite: Overwrite existing .webp files")
        print("\nExample: python convert_to_webp.py ./input ./output 90 --overwrite")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    quality = 85
    overwrite = False
    
    # Parse optional arguments
    for arg in sys.argv[3:]:
        if arg == '--overwrite':
            overwrite = True
        elif arg.isdigit():
            quality = int(arg)
            if quality < 1 or quality > 100:
                print("Error: Quality must be between 1 and 100")
                sys.exit(1)
    
    convert_to_webp(input_folder, output_folder, quality, overwrite)

if __name__ == "__main__":
    main()

