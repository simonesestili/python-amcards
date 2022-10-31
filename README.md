# See [Read the Docs](https://python-amcards.readthedocs.io/en/latest/) for full documentation
[![Read the Docs](images/readthedocs.png)](https://python-amcards.readthedocs.io/en/latest/)

## Installation
To install python-amcards, simply run this command in your terminal:  
```
$ pip install requests
```

## Usage
All interactions with the AMcards API are made through the AMcardsClient class.  

First, create an AMcardsClient as follows:  
```
>>> from amcards import AMcardsClient
>>> client = AMcardsClient('youraccesstoken')
```
Here `'youraccesstoken'` will be replaced with a string containing your AMcards access token. You can generate one [here](https://amcards.com/user/connected-applications/).
