Flask-Reggie
============


.. image:: https://travis-ci.org/rhyselsmore/flask-reggie.png?branch=master
        :target: https://travis-ci.org/rhyselsmore/flask-reggie

.. image:: https://pypip.in/d/Flask-Reggie/badge.png
        :target: https://crate.io/packages/Flask-Reggie/

Enable Regex Routes within Flask

Installation
------------

.. code-block:: bash

    pip install flask-redis


Configuration
-------------

To enable regex routes within your application

.. code-block:: python

    from flask import Flask
    from flask_reggie import Reggie

    app = Flask(__name__)
    Reggie(app)

or

.. code-block:: python

    from flask import Flask
    from flask_reggie import Reggie

    reggie = Reggie()

    def create_app():
        app = Flask(__name__)
        reggie.init_app(app)
        return app

Usage
-----

If we were looking to have a UUID supplied as a view argument, we would follow this pattern::

.. code-block:: python

    @app.route('/<regex("[0-9a-f]{32}"):uuid>')
    def example(uuid):
        return uuid

As you can see, we are able to supply a regular expression, and have it passed as a view argument.

Simple.