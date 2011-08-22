#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et

from setuptools import setup, find_packages
import st.log as package

setup(name=package.__package_name__,
      version=package.__version__,
      author=package.__author__,
      author_email=package.__email__,
      url=package.__url__,
      download_url='http://python.org/pypi/%s' % package.__package_name__,
      description=package.__summary__,
      long_description=package.__description__,
      license=package.__license__,
      platforms="OS Independent - Anywhere Python's Logging is known to run.",
      keywords = "Logging",
      namespace_packages = ["st"],
      packages = find_packages(),
      classifiers=[
          'Development Status :: 5 - Alpha',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Utilities',
      ]
)
