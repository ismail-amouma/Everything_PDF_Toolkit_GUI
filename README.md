# Everything ❤️ PDF Toolkit GUI

This is a simple graphical user interface (GUI) for the "Everything ❤️ PDF" toolkit that provides various functionalities to work with PDF documents. The GUI is built using the Tkinter library for Python and includes the following features:

## Features

1. Merge PDFs: Select multiple PDF files and merge them into a single PDF.
2. Split PDF: Choose a range of pages from a PDF file and create a new PDF containing those pages.
3. Compress PDF: Compress the content streams of each page in a PDF file to reduce file size.
4. PDF to Word: Convert a PDF file to a Word document (docx).
5. Word to PDF: Convert a Word document (docx) to a PDF file.
6. PDF to Image: Convert each page of a PDF file to a separate image (JPEG) and save them in a chosen output folder.

## Requirements

This GUI requires the following libraries to be installed:

- pathlib
- tkinter
- PyPDF2
- pdf2docx
- docx2pdf
- pdfrw
- pagelabels
- Pillow
- pdfium
- io
- pdf2image
- os

You can install these libraries using `pip`:

```
pip install pathlib2
pip install tk
pip install pypdf2
pip install pdf2docx
pip install docx2pdf
pip install pdfrw
pip install pagelabels
pip install Pillow
pip install pdfium2
pip install pdf2image
```

## How to use

1. Run the script, and a GUI window will appear.
2. Select the desired operation from the buttons provided.
3. Follow the prompts to choose input and output files or folders as required for each operation.
4. Depending on the operation, you may need to select specific pages or ranges.

## Important Note

The relative path for assets (images) used in the GUI has been set to the following location:

```
C:\frame0
```

Please ensure that the assets folder containing the images (`image_1.png`, `button_1.png`, `button_2.png`, `button_3.png`, `button_4.png`, `button_5.png`, `button_6.png`) is present at the above-mentioned location. If you prefer to use different images or change the location of the assets folder, please update the `ASSETS_PATH` variable in the script accordingly.

Feel free to use, modify, and extend this "I Love PDF" toolkit GUI to suit your specific needs. Enjoy working with PDFs!

## Disclaimer

This script and GUI are provided as-is and without warranty. Use it at your own risk. Make sure to take appropriate backups of your PDF files before using any operations that may modify or merge them.
