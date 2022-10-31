Getting Started
===============

Installation
------------
To install python-amcards, simply run this command in your terminal:

.. code-block::

    $ pip install requests

Usage
-----
All interactions with the AMcards API are made through the :ref:`AMcardsClient <amcards.AMcardsClient>` class.

First, create an :ref:`AMcardsClient <amcards.AMcardsClient>` as follows:

.. code-block::

    >>> from amcards import AMcardsClient
    >>> client = AMcardsClient('youraccesstoken')

Here ``'youraccesstoken'`` will be replaced with a string containing your AMcards access token. You can generate one `here <https://amcards.com/user/connected-applications/>`_.
