#!/usr/bin/env python3

import setuptools

install_requires = [
        ]

setuptools.setup(
    name="touchme",
    python_requires=">=3.9.10",
    description="Utility to create a new script based on a template",
    version="0.1",
    author="Kolja Hopfmann",
    author_email="",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'touchme = src.touchme:main',
        ],
    },
    include_package_data=True,
    )
