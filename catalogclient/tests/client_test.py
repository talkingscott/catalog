""" Tests for client """

# pylint: disable=R0903

import unittest

import client

class ClientTestCase(unittest.TestCase):
    """ Tests of CatalogClient """
    def setUp(self):
        self._transport = MockTransport()
        self._client = client.CatalogClient('/', self._transport)

    def test_get_items(self):
        """ Test the get_items method """
        items = self._client.get_items()
        self.assertEqual(len(items), 1)

    def test_get_item(self):
        """ Test the get_item method """
        item = self._client.get_item(987)
        self.assertIsInstance(item, dict)

    def test_get_no_item(self):
        """ Test the get_item method for a non-existent SKU """
        item = self._client.get_item(123)
        self.assertIsNone(item)

class MockTransport(client.ClientTransport):
    """ Mock transport for tests """

    def get_json(self, url):
        if url.endswith('/items'):
            return [
                {
                    'sku': 987,
                    'description': 'Spalding Basketball'
                }
            ]
        if url.endswith('/items/987'):
            return {
                'sku': 987,
                'description': 'Spalding Basketball'
            }
        if '/items/' in url:
            return {
                'status_code': 404,
                'body': ''
            }

        raise ValueError()
