import json
import pathlib
import pytest
from handler import ocr

@pytest.fixture
def lambda_event(request):
    file = pathlib.Path(request.node.fspath.strpath)
    event_file = file.with_name('extract-test-input.json')
    with event_file.open() as f:
        return json.load(f)

def test_handler(lambda_event):
    lambda_response = ocr(lambda_event, {})
    assert lambda_response['statusCode'] == 200
    assert len(lambda_response['body']['text']) > 0