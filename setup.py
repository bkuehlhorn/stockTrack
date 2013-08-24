#!/usr/bin/env python

import os
import sys

import stockTrack

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = stockTrack.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='stockTrack',
    version=version,
    description='Simple Stock Tracker Application',
    long_description=readme + '\n\n' + history,
    author='Bernard Kuehlhorn',
    author_email='bkuehlhorn@acm.org',
    url='https://github.com/bkuehlhorn/stockTrack',
    packages=[
        'stockTrack',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='stockTrack',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)