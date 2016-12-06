#!/usr/bin/env python

from setuptools import setup

setup(name='py2048-game',
      version='1.0.1',
      description='PyGTK implementation of the popular 2048 game',
      author='Ralph Embree',
      author_email='ralph.embree@brominator.org',
      url='https://github.com/ralphembree/py2048',
      scripts=['py2048'],
      keywords="py2048 2048 game gabriele cirulli",
      classifiers = [
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment :: Puzzle Games',
      ],
)
