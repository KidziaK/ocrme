import click
import pytesseract
import os

from pdf2image import convert_from_path

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('language', required=False, default="eng")
def ocrme(input_path: str, output_path: str, language: str) -> None:
    """
    OCRme: A CLI tool to extract text and math formulas from a PDF and save it as Markdown.
    """
    
    click.echo(f"Converting PDF '{input_path}' to images...")
    images = convert_from_path(input_path)

    ocr_text = ""

    click.echo("Performing OCR...")
    for i, image in enumerate(images):
        click.echo(f"Processing page {i + 1}...")
        config = r"--oem 3 --psm 6"
        text = pytesseract.image_to_string(image, config=config, lang=language)
        ocr_text += text + "\n\n"

    click.echo(f"Saving OCR result to '{output_path}'...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ocr_text)

    click.echo("OCR completed successfully!")

if __name__ == '__main__':
    ocrme()

