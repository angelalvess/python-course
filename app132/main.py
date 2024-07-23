from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

PASTA = Path(__file__).parent
PASTA_PDF = PASTA / 'pdf'
PDF = PASTA_PDF / 'R20240719.pdf'

PASTA_NOVA = PASTA / 'nova'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader((PDF))


writer = PdfWriter()

with open(PASTA_NOVA / 'novo.pdf', 'wb') as f:
    for page in reader.pages:
        writer.add_page(page)
        writer.write(f)
