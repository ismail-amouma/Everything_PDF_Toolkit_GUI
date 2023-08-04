
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from PyPDF2 import PdfReader,PdfWriter,PageObject
from pdf2docx import Converter
from docx2pdf import convert
import pdfrw 
from pagelabels import PageLabels, PageLabelScheme
from PIL import Image, ImageDraw, ImageFont
import pypdfium2 as pdfium
from io import BytesIO
from pdf2image import convert_from_path
import os
def merge_pdfs():
    pdf_files = filedialog.askopenfilenames(title="Select PDF files to merge", filetypes=[("PDF files", "*.pdf")])

    if pdf_files:
        pdf_writer = PdfWriter()

        for pdf_file in pdf_files:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

        output_file = filedialog.asksaveasfilename(title="Save Merged PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if output_file:
            with open(output_file, "wb") as out_pdf:
                pdf_writer.write(out_pdf)
            print("PDFs merged successfully.")


def split_pdf(start_page,end_page):
    pdf_file = filedialog.askopenfilename(title="Select PDF file to split", filetypes=[("PDF files", "*.pdf")])

    if pdf_file:
        pdf_reader = PdfReader(pdf_file)
        pdf_writer = PdfWriter()

        for page_num in range(start_page-1, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        output_file = filedialog.asksaveasfilename(title="Save Split PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if output_file:
            with open(output_file, "wb") as out_pdf:
                pdf_writer.write(out_pdf)
            print("PDFs split successfully.")
def compress_pdf():
    pdf_file = filedialog.askopenfilename(title="Select PDF file to compress", filetypes=[("PDF files", "*.pdf")])

    if pdf_file:
        pdf_reader = PdfReader(pdf_file)
        pdf_writer = PdfWriter()

        # Compress each page in the PDF
        for page in pdf_reader.pages:
            page.compress_content_streams()
            pdf_writer.add_page(page)

        output_file = filedialog.asksaveasfilename(title="Save Compressed PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if output_file:
            with open(output_file, "wb") as out_pdf:
                pdf_writer.write(out_pdf)
            print("PDF compressed successfully.")


def pdf_to_word():
    pdf_file = filedialog.askopenfilename(title="Select PDF file to convert", filetypes=[("PDF files", "*.pdf")])

    if pdf_file:
        output_file = filedialog.asksaveasfilename(title="Save Word Document", defaultextension=".docx", filetypes=[("Word files", "*.docx")])

        if output_file:
            # Perform the conversion
            cv = Converter(pdf_file)
            cv.convert(output_file)
            cv.close()

            print("PDF converted to Word successfully.")
def word_to_pdf():
    word_file = filedialog.askopenfilename(title="Select Word file to convert", filetypes=[("Word files", "*.docx")])

    if word_file:
        output_file = filedialog.asksaveasfilename(title="Save PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if output_file:
            # Perform the conversion using docx2pdf
            convert(word_file, output_file)

            print("Word document converted to PDF successfully.")
def convert_pdf_to_image():
    pdf_file = filedialog.askopenfilename(title="Select PDF file to convert", filetypes=[("PDF files", "*.pdf")])


    images = convert_from_path(pdf_file)
    output_folder_path = filedialog.askdirectory(title="Select output folder")
    os.makedirs(output_folder_path, exist_ok=True)

    for i in range(len(images)):
        image_path = os.path.join(output_folder_path, f"page_{i+1}.jpg")
        images[i].save(image_path, 'JPEG')
    print("PDF converted to image successfully.")
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ismail amouma\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("702x423")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 423,
    width = 702,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    351.0,
    211.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: merge_pdfs(),
    relief="flat"
)
button_1.place(
    x=34.5,
    y=112.5,
    width=187,
    height=124
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: split_pdf(1,2),
    relief="flat"
)
button_2.place(
    x=261.2799987792969,
    y=112.5,
    width=187,
    height=124
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: compress_pdf(),
    relief="flat"
)
button_3.place(
    x=488.04998779296875,
    y=112.5,
    width=187,
    height=124
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_pdf_to_image(),
    relief="flat"
)
button_4.place(
    x=34.5,
    y=255.32000732421875,
    width=187,
    height=124
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: word_to_pdf(),
    relief="flat"
)
button_5.place(
    x=261.2799987792969,
    y=255.32000732421875,
    width=187,
    height=124
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pdf_to_word(),
    relief="flat"
)
button_6.place(
    x=488.04998779296875,
    y=255.32000732421875,
    width=190,
    height=117
)
window.resizable(False, False)
window.mainloop()
