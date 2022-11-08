from pathlib import Path
from setuptools import setup

def README():
    with open('README.rst') as f:
        return f.read()

setup(
    name='python-amcards',
    version='1.2.3',
    description='A wrapper for the AMcards API.',
    long_description=README(),
    long_description_content_type='text/x-rst',
    author='Simone Sestili',
    author_email='simone.sestili@amcards.com',
    url='https://github.com/simonesestili/python-amcards',
    packages=['amcards'],
    package_dir={'amcards': 'amcards'},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=['requests>=2'],
)
