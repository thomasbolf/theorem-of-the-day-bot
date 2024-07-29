import requests
from pathlib import Path
from pdf2image import convert_from_path

URL = "http://www.theoremoftheday.org/todays.php"

def fetch_pdf_and_save():
    response = requests.get(URL, allow_redirects=True)
    response.raise_for_status()  # Ensure we notice bad responses
    filename = Path("totd.pdf")
    filename.write_bytes(response.content)

def pdf_to_image():
    convert_from_path("totd.pdf")[0].save("totdImage.png")

def save_daily_image():
    fetch_pdf_and_save()
    pdf_to_image()
    return True