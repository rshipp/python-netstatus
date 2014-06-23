import os
from setuptools import setup

from netstatus import __version__

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='netstatus',
    version=__version__,
    packages=['netstatus', 'netstatus.services'],
    include_package_data=True,
    install_requires=[],
    license='New BSD',
    description='Check and report on the status of network devices.',
    long_description=README,
    url='https://github.com/george2/python-netstatus',
    author='george2',
    author_email='rpubaddr0@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
    ],
)
