# Import the base64 encoding library.
import os
import io
from dotenv import load_dotenv
from google.cloud import vision

load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS')

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    image_path = os.path.join(os.getcwd(), path)
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(response.error.message))
    
    text_content = ""
    for text in texts:
        text_content += text.description + " "

    return text_content
    
   