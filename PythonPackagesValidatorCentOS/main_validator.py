'''
Created on Jun 23, 2017

@author: sfurman


The CentOS7 Python packages easy fix script.
'''

import platform
import sys
from subprocess import Popen, PIPE


def sys_platform_version_info():
    print('%s.%s.%s' % (sys.version_info[0],
                        sys.version_info[1],
                        sys.version_info[2]))
    print('%s, %s' % (platform.architecture()[0],
                      platform.architecture()[1]))


def validator(input_file):
    with open(input_file) as f:
        for package_name in f:
            package_name_formatted = package_name.rstrip()
            print('Package: %s : %s' % (package_name_formatted, run_command(package_name_formatted)))


def run_command(package_name):
    # rpm -V package_name
    p = Popen(['rpm', '-V', package_name], stdout=PIPE)
    out, err = p.communicate()

    if len(out) == 0:
        return 'VALIDATED'
    else:
        return out.decode()


if __name__ == '__main__':
    sys_platform_version_info()
    if raw_input('Did you run: # rpm -qa python\* > installed_python_packages.txt command first?') != 'y':
        exit(0)

    validator('installed_python_packages.txt')

    print('\nEach package that is not VALIDATED should be reinstalled.'
          '\nCommand: # yum reinstall package_name.'
          '\nExample: # yum reinstall python-pyudev-0.15-9.el7.noarch\n'
          '\nMissing packages could be deleted or reinstalled, but be careful!\n'
          '\nIn the end, run validator to confirm package validity.')

# Get a list of the currently installed python packages and write them into
# installed_python_packages.txt file:
# rpm -qa python\* > installed_python_packages.txt

# Run script:
# python main_validator.py

# Watch the output.
