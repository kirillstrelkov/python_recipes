import codecs
import os
import shutil
from distutils import dir_util


def get_files_and_subfiles(folder, suffix, recursively=True):
    files = []
    if recursively:
        for root, _, dirfiles in os.walk(folder):
            for filename in dirfiles:
                path = os.path.join(root, filename)
                if file_ends_with(path, suffix):
                    files.append(path)
    else:
        files += [os.path.join(folder, f) for f in os.listdir(folder)
                  if file_ends_with(os.path.join(folder, f), suffix)]

    return files


def file_ends_with(path, suffix):
    return path.endswith(suffix)


def relpath2abspath(path):
    if path and isinstance(path, basestring if os.sys.version_info[0] == 2 else str):
        return os.path.abspath(os.path.expanduser(path))
    else:
        return path


def validate_paths_exist(*paths):
    for path in paths:
        if path and not os.path.exists(path):
            raise IOError("Path '{}' doesn't exist.".format(path))


def rm_if_exists(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def copy(src, dst, verbose=False):
    src = relpath2abspath(src)
    dst = relpath2abspath(dst)
    if verbose:
        print('Copying {} -> {}'.format(src, dst))
    if not os.path.exists(src):
        raise IOError("File '{}' does not exist".format(src))
    if os.path.isdir(src):
        dir_util.copy_tree(src, os.path.join(dst, os.path.basename(src)))
    else:
        shutil.copy(src, dst)


def read_content(path):
    with codecs.open(path, encoding="utf8", mode='r') as f:
        return f.read()


def save_file(path, content):
    with codecs.open(path, encoding="utf8", mode='w') as f:
        f.write(content)


def read_lines(path):
    with codecs.open(path, 'r', encoding='utf8') as f:
        return f.read_lines()


def read_file(path):
    with codecs.open(path, 'r', encoding='utf8') as f:
        return f.read()


def append_to_file(path, content):
    with codecs.open(path, encoding="utf8", mode='a') as f:
        f.write(content)
