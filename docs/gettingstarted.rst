Getting Started
===============

Installation
------------
To install python-amcards, simply run this command in your terminal:

.. code-block::

    $ pip install python-amcards

Usage
-----
All interactions with the AMcards API are made through the :ref:`AMcardsClient <amcards.AMcardsClient>` class.

First, create an :ref:`AMcardsClient <amcards.AMcardsClient>` as follows:

.. code-block::

    >>> from amcards import AMcardsClient
    >>> client = AMcardsClient('youraccesstoken')

Here ``'youraccesstoken'`` will be replaced with a string containing your AMcards access token. You can generate one `here <https://amcards.com/user/connected-applications/>`_.

Now we can perform all operations supported by the :ref:`client <amcards.AMcardsClient>`.

Let's try using ``send_card`` to send a card to a single recipient:

.. code-block::

        >>> res = client.send_card(
        ...     template_id='123',
        ...     initiator='myintegration123',
        ...     shipping_address={
        ...         'first_name': 'Ralph',
        ...         'last_name': 'Mullins',
        ...         'address_line_1': '2285 Reppert Road',
        ...         'city': 'Southfield',
        ...         'state': 'MI',
        ...         'postal_code': '48075',
        ...         'country': 'US'
        ...     }
        ... )
        >>> res.card_id
        1522873
        >>> res.total_cost
        442
        >>> res.message
        'Card created successfully!'
        >>> res.user_email
        'example@example.com'
        >>> res.shipping_address
        {'last_name': 'Mullins', 'address_line_1': '2285 Reppert Road', 'first_name': 'Ralph', 'country': 'US', 'state': 'MI', 'postal_code': '48075', 'city': 'Southfield'}
