from pathlib import Path
from setuptools import setup

def README():
    with open('README.md') as f:
        return f.read()

setup(
    name='python-amcards',
    version='0.1.2',
    description='A wrapper for the AMcards API.',
    long_description=README(),
    long_description_content_type='text/markdown',
    author='Simone Sestili',
    author_email='simone.sestili@amcards.com',
    url='https://github.com/simonesestili/python-amcards',
    py_modules=['amcards'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=['requests'],
)
