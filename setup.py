#!/usr/bin/env python

PROJECT = 'SPARQLginger'

# Change docs/sphinx/conf.py too!
VERSION = '0.01'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Generate dynamic HTML data sites from SPARQL queries',
    long_description=long_description,

    author='Scott Ogle',
    author_email='scott@semanticarts.com',

    # url='https://github.com/dreamhost/cliff',
    # download_url='https://github.com/dreamhost/cliff/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    # entry_points={
    #     'console_scripts': [
    #         'ginger = SPARQLginger.main:main'
    #     ],
    #     'cliff.demo': [
    #         'simple = cliffdemo.simple:Simple',
    #         'two_part = cliffdemo.simple:Simple',
    #         'error = cliffdemo.simple:Error',
    #         'list files = cliffdemo.list:Files',
    #         'files = cliffdemo.list:Files',
    #         'file = cliffdemo.show:File',
    #         'show file = cliffdemo.show:File',
    #         'unicode = cliffdemo.encoding:Encoding',
    #     ],
    # },

    entry_points={
        'console_scripts': [
            'ginger = SPARQLginger.main:main'
        ],
        'ginger': [
            'new = SPARQLginger.create:Create',
            'build = SPARQLginger.build:Build',
            'serve = SPARQLginger.serve:Serve'
        ]
    },

    zip_safe=False,
)
