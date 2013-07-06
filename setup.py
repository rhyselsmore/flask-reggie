#!/usr/bin/env python

"""
Flask-Reggie
------------

Quickly and Easily enable Regex Routes within your Flask Application

"""

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='Flask-Reggie',
    version='0.0.2',
    url='http://github.com/rhyselsmore/flask-reggie',
    author='Rhys Elsmore',
    author_email='me@rhys.io',
    description='Flask Regex Routes.',
    long_description=open('README.rst').read() + '\n\n' +
        open('HISTORY.rst').read(),
    py_modules=['flask_reggie'],
    license=open('LICENSE').read(),
    package_data={'': ['LICENSE']},
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
