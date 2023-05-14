# -*- coding: utf-8 -*-

"""
    Setup

    Virtual environment activation:
        [sfurman@localhost seven_segment_display]$ source ~/Py_3.8_env/bin/activate

    Cleaning (optional):
        (Py_3.8_env) [sfurman@localhost seven_segment_display]$
            rm -rf dist/ build/

    Create wheel:
        (Py_3.8_env) [sfurman@localhost seven_segment_display]$
            python setup.py bdist_wheel

    Install wheel in /home/sfurman/Py_3.8_env/lib/python3.8/site-packages:
        (Py_3.8_env) [sfurman@localhost seven_segment_display]$
            pip install dist/seven_segment_display-1.0.0-py3-none-any.whl
            or:
            pip install dist/seven_segment_display-1.0.0-py3-none-any.whl --force-reinstall

    Install location:
        /home/sfurman/Py_3.8_env/lib/python3.8/site-packages/seven_segment_display-1.0.0.dist-info
"""

from setuptools import setup, find_packages

setup(
    name='seven_segment_display',
    version='1.0.0',

    packages=find_packages(include=['common', 'graphic', 'device'],
                           exclude=['*run*', '*tests*']),

    url='',
    license='',
    author='sfurman',
    author_email='',
    description=''
)
