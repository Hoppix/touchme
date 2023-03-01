#!/usr/bin/env python3

import setuptools

install_requires = [
        ]

setuptools.setup(
    name="touchsh",
    description="Utility to create a new script based on a shell script template",
    version="0.1",
    author="Kolja Hopfmann",
    author_email="",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'touchsh = src.touchsh:main',
        ],
    },
    include_package_data=True,
    )
