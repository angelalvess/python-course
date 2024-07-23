from PIL import Image

from pathlib import Path

ROOT = Path(__file__).parent
ORIGINAL_IMAGE = ROOT / 'aes.jpg'
NEW_IMAGE = ROOT / 'aes_new.jpg'

pillow_image = Image.open(ORIGINAL_IMAGE)
width, height = pillow_image.size

new_width = 640
new_height = height * new_width // width

new_image = pillow_image.resize((new_width, new_height))
new_image.save(NEW_IMAGE, optimize=True, quality=90
               )
