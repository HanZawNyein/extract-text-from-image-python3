from PIL import Image
from pytesseract import pytesseract

def extract_text_from_image(image_path:str)->str:
    return pytesseract.image_to_string(Image.open(image_path))

if __name__ == "__main__":
    path_to_image = 'images/image.png'
    print(extract_text_from_image(image_path=path_to_image))