# pylint: disable=C0111

import json
import unittest

import server

from bottle import HTTPResponse

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        server.initdb('schema-version-items.json')

    def test_get_items(self):
        items = _parsed_json(server.get_items())
        self.assertEqual(len(items), 1)

    def test_get_item(self):
        item = _parsed_json(server.get_items(9876))
        self.assertEqual(item['description'], 'Product X')

    def test_get_none(self):
        item = server.get_items(1234)
        self.assertIsInstance(item, HTTPResponse)
        self.assertEqual(item.status_code, 404)

def _parsed_json(resp):
    # N.B. this does not handle all possible cases
    if isinstance(resp, HTTPResponse):
        resp = resp.body
    if isinstance(resp, str):
        resp = json.loads(resp)
    return resp
