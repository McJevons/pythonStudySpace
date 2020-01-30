import tesserocr
from PIL import Image

image = Image.open('F:\\abc.png')
result = tesserocr.image_to_text(image)
print(result)
