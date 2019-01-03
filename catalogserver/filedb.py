"""
Simple implementation of a database based on a JSON file.
"""

import json
from typing import Any, Dict, Optional, Sequence

class FileDB:
    """
    A read-only database based on a JSON file.
    """
    def __init__(self, filename: str) -> None:
        self._filename = filename
        with open(filename, 'r') as fp: # pylint: disable=C0103
            self._data = json.load(fp)
            self._schema_version = self._data['schema-version']
            if self._schema_version.startswith('1.0.'):
                self._items = self._data['items']
            else:
                raise ValueError()

    def get_item(self, sku: int) -> Optional[Dict[str, Any]]:
        """ Gets an item from the database, or None """
        for item in self._items:
            if item['sku'] == sku:
                return item
        return None

    def get_items(self) -> Sequence[Dict[str, Any]]:
        """ Gets all the items in the database """
        return self._items

    @property
    def filename(self) -> str:
        """ Gets the filename that contains the data """
        return self._filename

    def __str__(self):
        return self._filename
