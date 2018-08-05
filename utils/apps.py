import os
import subprocess
from subprocess import Popen, PIPE

from utils.file import validate_paths_exist


def call_binary(binary_name, binary_args, install_path=None, verbose=False):
    if install_path:
        binary = os.path.join(install_path, binary_name)
        validate_paths_exist(binary)
    else:
        binary = binary_name
    command = [binary] + binary_args
    if verbose:
        print(' '.join(command))
    try:
        subprocess.check_call(command)
        return True
    except subprocess.CalledProcessError:
        print("Failed to execute: {}".format(command))
        return False


def execute_cmd(cmd, **kwargs):
    kwargs['stdout'] = PIPE
    kwargs['stderr'] = PIPE
    p = Popen(cmd, **kwargs)
    stdout, stderr = p.communicate()
    code = p.returncode
    return code, stdout, stderr
