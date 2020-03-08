#!/usr/bin/env python

"""
Created on Jun 23, 2017

@author: sfurman


The CentOS7 Python packages easy fix script.

Example usage
  Get a list of the currently installed python packages and write it into
  installed_python_packages.txt file:
  rpm -qa python\* > installed_python_packages.txt

  Run script:
  python main_validator.py
  Watch the output.
"""

import platform
import sys
from subprocess import Popen, PIPE

from colors import Color


# from colorama import init

# init()


def sys_platform_version_info():
    print('Python: %s.%s.%s' % (sys.version_info[0],
                                sys.version_info[1],
                                sys.version_info[2]))
    print('Architecture: %s, %s' % (platform.architecture()[0],
                                    platform.architecture()[1]))


def validator(input_file):
    with open(input_file) as f:
        for package_name in f:
            package_name_formatted = package_name.rstrip()
            print('Package: %s : %s' % (package_name_formatted,
                                        run_command(package_name_formatted)))


def run_command(package_name):
    # rpm -V package_name
    p = Popen(['rpm', '-V', package_name], stdout=PIPE)
    out, err = p.communicate()

    if len(out) == 0:
        return color.TEXT_GREEN + 'VALIDATED' + color.TEXT_RESET
    else:
        return color.TEXT_RED + out.decode() + color.TEXT_RESET


if __name__ == '__main__':
    color = Color()

    sys_platform_version_info()

    print (color.TEXT_CYAN +
           'Python Package Validator for CentOS.\n' + color.TEXT_RESET)

    if raw_input(color.TEXT_MAGENTA +
                 '\nDid you run below command as sudo first? (y/n)\n'
                 'rpm -qa python\* > installed_python_packages.txt\n' +
                 color.TEXT_RESET) != 'y':
        exit(0)

    validator('installed_python_packages.txt')

    print(color.TEXT_BLUE +
          '\nClosing Message'
          '\n  Each package that is not VALIDATED should be reinstalled.'
          '\n  Command: # yum reinstall package_name'
          '\n  Example: # yum reinstall python-pyudev-0.15-9.el7.noarch'
          '\n  Missing packages could be deleted or reinstalled, but be careful!'
          '\n  In the end, run Python Package Validator again to confirm package validity.' +
          color.TEXT_RESET)
