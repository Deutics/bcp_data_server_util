from distutils.core import setup
from setuptools import find_packages
import os

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''
setup(

    # Project name:
    name='bcp-data-server',

    # Packages to include in the distribution:
    packages=find_packages(),

    # Project version number:
    version='1.0.14',

    # List a license for the project, eg. MIT License
    license='MIT',

    # Short description of your library:
    description='A package for making api requests to BCP data server',

    # Long description of your library:
    long_description=long_description,
    long_description_content_type='text/markdown',

    # Your name:
    author='Peterlight Faboyede',

    # Your email address:
    author_email='petlight49@gmail.com',

    # Link to your github repository or website:
    url='https://github.com/Deutics/bcp_data_server_util.git',

    # Download Link from where the project can be downloaded from:
    download_url='',

    # List of keywords:
    keywords=[],

    # List project dependencies:
    install_requires=[
        'requests',
        'pytz',
        'python-dateutil'
    ],

    # https://pypi.org/classifiers/
    classifiers=[],
    zip_safe=False
)
