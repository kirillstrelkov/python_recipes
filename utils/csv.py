import codecs
from csv import DictReader, DictWriter

from itertools import islice


def get_row_dict_from_csv(path, header=None, skip_first_row=False):
    with codecs.open(path, 'r', 'utf8') as f:
        if skip_first_row:
            f = islice(f, 1, None)
        reader = DictReader(f, fieldnames=header)
        for row in reader:
            yield row


def save_dicts(path, dicts):
    with codecs.open(path, 'wb', 'utf8') as f:
        writer = None
        for d in dicts:
            if d:
                if writer is None:
                    writer = DictWriter(f, sorted(d.keys()))
                    writer.writeheader()
                writer.writerow(d)
