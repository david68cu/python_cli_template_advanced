 -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python CLI',
    long_description=readme,
    author='David Gutierrez',
    author_email='david@pythonsoftware.solutions',
    url='https://github.com/david68cu/samplecli',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points = {
         'console_scripts': [
             'sample = core.__main__:main'
         ]}
)
