"""
Simple client for catalog server.
"""
# pylint: disable=R0903

import abc
import logging
from typing import Any, Mapping, Optional, Sequence, Union
import requests

CATALOG_SERVER_BASE_URL = 'http://localhost:8123/'

class ClientTransport:
    """ Abstract transport for CatalogClient """

    @abc.abstractmethod
    def get_json(self, url: str) -> Union[Sequence[Mapping[str, Any]], Mapping[str, Any]]:
        """ Gets JSON from a URL """
        return {}

class RequestsTransport(ClientTransport):
    """ ClientTransport that uses requests package """

    def get_json(self, url: str) -> Union[Sequence[Mapping[str, Any]], Mapping[str, Any]]:
        resp = requests.get(url)
        logging.debug(resp.status_code)
        logging.debug(resp.headers)
        if resp.status_code >= 200 and resp.status_code < 300:
            logging.debug(resp.json())
            return resp.json()

        logging.debug(resp.text)
        return {
            "status_code": resp.status_code,
            "text": resp.text
        }

class CatalogClient:
    """
    Simple client for catalog server.
    """
    def __init__(self, base_url: str, transport: ClientTransport) -> None:
        self._base_url = base_url
        self._transport = transport

    @property
    def base_url(self) -> str:
        """ Gets the base URL """
        return self._base_url

    def get_items(self) -> Sequence[Mapping[str, Any]]:
        """ Gets the full catalog """
        url = self._base_url + 'items'
        resp = self._transport.get_json(url)
        if not isinstance(resp, list):
            raise TypeError()
        return resp

    def get_item(self, sku: str) -> Optional[Mapping[str, Any]]:
        """ Gets one item or None """
        url = f'{self._base_url}items/{sku}'
        resp = self._transport.get_json(url)
        if not isinstance(resp, dict):
            raise TypeError()
        if 'status_code' in resp:
            if resp['status_code'] == 404:
                return None
            raise ValueError(resp['status_code'])
        return resp

    def __str__(self):
        return self._base_url

def _main():
    client = CatalogClient(CATALOG_SERVER_BASE_URL, RequestsTransport())
    all_items = client.get_items()
    print(all_items)
    one_item = client.get_item(1234)
    print(one_item)
    no_item = client.get_item(9876543)
    print(no_item)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _main()
