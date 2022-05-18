import base64
import requests

with open('index.png', 'rb') as file:
    base64_str = base64.b64encode(file.read()).decode()

response = requests.post(
    'https://0bmg3xpb9k.execute-api.eu-west-2.amazonaws.com/dev/ocr',
    json={
        'image': base64_str
    }
)

print(response.json())