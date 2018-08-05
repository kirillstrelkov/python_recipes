import re
from subprocess import check_output

from utils.apps import call_binary, execute_cmd


def exec(cmd):
    return execute_cmd('{} || true'.format(cmd), shell=True)


def get_apps(output, index):
    output = output.decode('utf8')
    apps = []
    for row in output.splitlines():
        cols = re.split('\s+', row)
        if len(cols) > 1:
            app = cols[index]
            apps.append(app)
    return apps


if __name__ == '__main__':
    cmd_to_remove = ['sudo apt purge']
    dpkg_apps = get_apps(exec('dpkg -l')[1], 1)
    for dpkg_app in dpkg_apps:
        # print(dpkg_app)
        snap_output = exec('snap find {}'.format(dpkg_app))[1]
        # if 'No matching snaps' not in snap_output:
        snap_apps = get_apps(snap_output, 0)
        if dpkg_app in snap_apps:
            print("FOUND: dpkg app: {}\t\tsnaps: {}".format(dpkg_app, ', '.join(snap_apps)))
            cmd_to_remove.append(dpkg_app)

    print(' '.join(cmd_to_remove))
