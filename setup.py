#!/usr/bin/python
# -*-coding:UTF-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='name-cleaver',
    version='0.6.0',
    description='A fork of name-cleaver, with family name support.',
    long_description=readme,
    author='Alison Rowland',
    author_email='arowland@sunlightfoundation.com',
    url='http://github.com/ligyxy/name-cleaver/',
    packages=find_packages(),
    license='BSD License',
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Topic :: Text Processing :: Linguistic',
    ],
)

