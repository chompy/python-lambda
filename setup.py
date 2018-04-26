#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pip

from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = parse_requirements(
    "requirements.txt", session=PipSession()
)
pip_requirements = [str(r.req) for r in requirements]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python-lambda',
    version='0.8.1',
    description="The bare minimum for a Python app running on Amazon Lambda.",
    long_description=readme,
    author="Nick Ficano",
    author_email='nficano@gmail.com',
    url='https://github.com/nficano/python-lambda',
    packages=find_packages(),
    package_data={
        'aws_lambda': ['project_templates/*'],
        '': ['*.json'],
    },
    include_package_data=True,
    scripts=['scripts/lambda'],
    install_requires=pip_requirements,
    license="ISCL",
    zip_safe=False,
    keywords='python-lambda',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
