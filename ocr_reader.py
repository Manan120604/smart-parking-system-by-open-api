import easyocr
reader = easyocr.Reader(['en'])

def extract_plate(image_path: str):
    results = reader.readtext(image_path)
    for bbox, text, conf in results:
        if 6 < len(text) <= 10:
            return text.upper()
    return None
