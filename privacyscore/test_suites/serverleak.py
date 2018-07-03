import json
import subprocess
from typing import Dict, Union

test_name = 'serverleak'
test_dependencies = []


def test_site(url: str, previous_results: dict, **options) -> Dict[str, Dict[str, Union[str, bytes]]]:
    result = subprocess.check_output([
        'snallygaster',
        '-j',
        url])
    return {
        'url': {
            'mime_type': 'text/plain',
            'data': url.encode(),
        },
        'jsonresult': {
            'mime_type': 'application/json',
            'data': result
        }
    }


def process_test_data(raw_data: list, previous_results: dict, **options) -> Dict[str, list]:
    leaks = []
    result = {}

    data = json.loads(raw_data['jsonresult']['data'])

    for entry in data:
        leaks.append(entry['cause'])

    result['leaks'] = leaks
    return result
