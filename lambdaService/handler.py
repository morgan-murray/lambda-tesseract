import base64
import json
import os
import pytesseract

from PIL import Image
from io import BytesIO

if os.getenv('AWS_EXECUTION_ENV') is not None:
    os.environ['LD_LIBRARY_PATH'] = '/opt/lib'
    os.environ['TESSDATA_PREFIX'] = '/opt/tessdata'
    pytesseract.pytesseract.tesseract_cmd = '/opt/tesseract-standalone'

def ocr(event, context):
        
    request_body = json.loads(event['body'])
    img_byteIO = BytesIO(base64.b64decode(request_body['image']))
    img = Image.open(img_byteIO)

    custom_config = r'--oem 3 --psm 6'
    converted = pytesseract.image_to_string(img, config=custom_config)

    body = {
        "text": converted
    }

    return {
        'statusCode': 200,
        'body': body
    }
