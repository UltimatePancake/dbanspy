Discordlist Bans Python
=======================

DBans is a simple API wrapper for `DiscordList Bans`_, more info about
DBans you can find there.

Installation:
-------------

pip:
~~~~

.. code:: bash

    $ pip install dbans

Manual Install:
~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/JustMaffie/dbanspy && cd dbanspy
    $ pip install .

Examples:
-------------

.. code:: py

    from dbans import DBans

    dBans = DBans(token="token here")
    print(dBans.lookup("user id here"))

.. _DiscordList Bans: https://bans.discordlist.net