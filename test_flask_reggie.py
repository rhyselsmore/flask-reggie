#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import flask
from flask import Flask, request
from flask_reggie import Reggie


def create_app():
    if "0.8" in flask.__version__:
        return Flask('test_flask_reggie')
    return Flask('test-flask-reggie')


class FlaskReggieTestCase(unittest.TestCase):

    def setUp(self):
        """ Construct our Flask Test App """

        self.app = create_app()
        reggie = Reggie()
        reggie.init_app(self.app)

        @self.app.route('/<regex("[abc0-9]{1,3}"):test>')
        def index(test):
            return "ok"

        self.client = self.app.test_client()

    def test_valid_pattern(self):
        with self.app.test_client() as c:
            rv = c.get('/ab1')
            assert rv.data == "ok"
            assert request.view_args['test'] == "ab1"

    def test_invalid_pattern(self):
        with self.app.test_client() as c:
            rv = c.get('/ad1')
            assert rv.status_code == 404

if __name__ == '__main__':
    unittest.main()
