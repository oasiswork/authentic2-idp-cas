#!/usr/bin/python
from setuptools import setup, find_packages
import os

setup(name='authentic2-idp-cas',
        version='1.0',
        license='AGPLv3',
        description='Authentic2 IdP CAS',
        author="Entr'ouvert",
        author_email="info@entrouvert.com",
        packages=find_packages(os.path.dirname(__file__) or '.'),
        install_requires=[
        ],
        entry_points={
            'authentic2.plugin': [
                'authentic2-idp-cas = authentic2_idp_cas:Plugin',
            ],
        },
)
