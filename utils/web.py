import codecs
import shutil
from urllib.parse import quote_plus

import requests


def get_json_from_url(url):
    resp = requests.get(url)
    return resp.json()


def get_text_from_url(url):
    resp = requests.get(url)
    return resp.text


def test_url_exists(url, auth=None):
    resp = requests.get(url, auth=auth, verify=False)
    return resp.status_code == 200


def download_file(url, output):
    print('Downloading {} -> {}'.format(url, output))
    with codecs.open(output, 'wb') as f:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


def quote_url(url):
    return quote_plus(url)
