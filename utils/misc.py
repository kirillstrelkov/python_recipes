import os
import re
import collections

from multiprocessing.pool import Pool

from multiprocessing import cpu_count


def parse_int(text):
    found = re.findall('\d+', text)
    if len(found) > 0:
        return int(found[0])
    else:
        return None


def print_with_prefix(message, prefix='', skip_prefix=False):
    if skip_prefix:
        print("{}".format(message))
    else:
        if prefix == '':
            print("{:>16s} {}".format(prefix, message))
        else:
            print("{:>15s}: {}".format(prefix, message))


def get_value_from_list_of_dicts(list_with_dicts, key, default=None):
    for d in list_with_dicts:
        value = d.get(key)
        if value is not None:
            return value
    return default


def get_dict_from_list_of_dicts(list_with_dicts, sub_dict, default=None):
    for d in list_with_dicts:
        if all(item in d.items() for item in sub_dict.items()):
            return d
    return default


def is_win():
    return os.sys.platform.startswith('win')


def concurrent_map(func, iterable):
    return Pool(cpu_count() - 1).map(func, iterable)


def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

