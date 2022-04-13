import os
import io
from dotenv import load_dotenv
from google.cloud import vision

load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS', 'creds.json')


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    image_path = os.path.join(os.getcwd(), path)
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(response.error.message))

    return response.full_text_annotation.text
