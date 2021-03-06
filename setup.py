#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = '0.0.6'

setup(
    name='webnsock',
    packages=find_packages(),
    version=VERSION,
    entry_points={
        'console_scripts':
            [
                'webnsock=webnsock:main',
            ]
    },

    install_requires=['web.py', 'trollius;python_version<"3.6"', 'autobahn'],
    description='A web.py and websocket framework for interactive webservices',
    author='Marc Hanheide',
    author_email='marc@hanheide.net',
    url='https://github.com/marc-hanheide/webnsock',
    download_url='https://github.com/marc-hanheide/webnsock/archive/%s.tar.gz'
        % VERSION,  # I'll explain this in a second
    keywords=['web.py', 'websockets', 'webserver'],  # arbitrary keywords
    classifiers=[],
    include_package_data=True,
    zip_safe=False
)
