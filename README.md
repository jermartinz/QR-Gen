# QR Code Generator

A simple Python program that generates QR codes in two formats: ASCII art for terminal display and PNG images for saving.

## Features

- Generate QR codes as ASCII art for terminal viewing
- Save QR codes as PNG image files
- Interactive menu-driven interface
- Support for any text or URL input

## Requirements

- Python 3.x
- `qrcode` library

## Installation

1. Install the required dependency:
```bash
pip install qrcode[pil]
```

2. Run the program:
```bash
python qr_code.py
```

## Usage

1. Run the script and choose from the menu:
    - **Option 1**: Generate ASCII art QR code (displays in terminal)
    - **Option 2**: Generate PNG image QR code (saves to file)
    - **Option 3**: Exit the program

2. Enter the text or URL you want to encode

3. For PNG output, specify the filename when prompted

## Example

```
==== QR Code Generator ====
Choose output format - (1) ASCII Art, (2) PNG Image, (3) Exit: 1
Enter the text or URL to encode in the QR code: https://github.com
```

The program will display the QR code as ASCII characters in your terminal or save it as a PNG file.