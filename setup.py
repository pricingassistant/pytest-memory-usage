#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-memory-usage',
    version='0.1.0',
    author='Eli Boyarski',
    author_email='eli.boyarski@gmail.com',
    maintainer='Eli Boyarski',
    maintainer_email='eli.boyarski@gmail.com',
    license='GNU GPL v3.0',
    url='https://github.com/eli-b/pytest-memory-usage',
    description='Reports test memory usage, and adds memory bounds',
    long_description=read('README.rst'),
    py_modules=['pytest_memory_usage'],
    install_requires=['pytest>=2.9.2', 'psutil>=4.3.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    entry_points={
        'pytest11': [
            'memory-usage = pytest_memory_usage',
        ],
    },
)
