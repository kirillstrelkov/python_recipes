import codecs
import json
from csv import DictWriter


def json2csv(json_path, csv_path):
    obj = json.load(codecs.open(json_path, encoding='utf8'))
    if len(obj):
        with codecs.open(csv_path, mode='wb', encoding='utf8') as f:
            writer = DictWriter(f, sorted(obj[0].keys()))
            writer.writeheader()
            writer.writerows(obj)


def read_json(path=None, string=None):
    if path:
        with codecs.open(path, encoding='utf8') as data_file:
            return json.load(data_file)
    if string:
        return json.loads(string, encoding='utf8')


def save_json(path, json_obj):
    with codecs.open(path, 'w', 'utf8') as f:
        f.write(json.dumps(json_obj, indent=4))
