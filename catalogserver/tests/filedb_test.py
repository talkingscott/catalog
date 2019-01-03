# pylint: disable=C0111

import unittest

from filedb import FileDB

class FileDBTestCase(unittest.TestCase):

    def test_file_not_exists(self):
        with self.assertRaises(IOError):
            _ = FileDB('file not there')

    def test_empty(self):
        with self.assertRaises(KeyError):
            _ = FileDB('empty.json')

    def test_schema_version_items(self):
        filedb = FileDB('schema-version-items.json')
        self.assertEqual(len(filedb.get_items()), 1)

    def test_schema_version_item(self):
        filedb = FileDB('schema-version-items.json')
        self.assertIsInstance(filedb.get_item(9876), dict)

if __name__ == '__main__':
    unittest.main()
