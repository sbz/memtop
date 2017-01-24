#!/usr/bin/env python

from setuptools import setup

__name__ = 'memtop'
__version__ = '0.0.1'
__author__ = 'Sofian Brabez'
__author_email__ = 'sbz@6dev.net'
__desc__ = 'memory top(1) like in Python'
__url__ = 'https://github.com/sbz/memtop'


classifiers = """
Development Status :: 1 - Alpha
Intended Audience :: System Administrators
Topic :: System :: Systems Administration
License :: OSI Approved :: BSD License
Programming Language :: Python :: 2.7,
Programming Language :: Python :: 3.5,
""".split("\n")

def get_contents(file_path):
    data = None
    with open(file_path, 'r') as fd:
        data = fd.read()
    return data

setup_opts = {
    'name': __name__,
    'version':  __version__,
    'description':  __desc__,
    'long_description': get_contents('README.md'),
    'author':   __author__,
    'author_email': __author_email__,
    'url':  __url__,
    'license': 'BSD',
    'scripts': ['bin/memtop'],
    'install_requires': [
        'psutil',
    ],
    'classifiers': classifiers,
}

setup(**setup_opts)
