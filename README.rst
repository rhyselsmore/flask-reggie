Flask-Reggie
========

.. image:: https://secure.travis-ci.org/rhyselsmore/flask-reggie.png?branch=master

*Under Construction*

Enable Regex Routes within Flask

Installation
------------

Installation occurs via 1 command::

    pip install flask-reggie

Configuration
-----------

Follow the typical pattern for installing Flask extensions::

    from flask import Flask
    from flask_reggie import Reggie

    app = Flask(__name__)
    reggie = Reggie(app)

*or*::

    from flask import Flask
    from flask_reggie import Reggie

    app = Flask(__name__)
    reggie = Reggie()
    reggie.init_app(app)

Usage
-----

If we were looking to have a UUID supplied as a view argument, we would follow this pattern::

    @app.route('/<regex("[0-9a-f]{32}"):uuid>')
    def example(uuid):
        return uuid

As you can see, we are able to supply a regular expression, and have it passed as a view argument.

Simple.