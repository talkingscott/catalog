"""
Trivial catalog server.
"""
import json

from filedb import FileDB

from bottle import Bottle, HTTPResponse, run

CATALOG_FILE = 'catalog.json'

app = Bottle()  # pylint: disable=C0103

@app.get('/items')
@app.get('/items/<sku>')
def get_items(sku=None):
    """ Gets one or all the catalog items """
    if sku:
        item = filedb.get_item(int(sku))
        if item:
            return item
        return HTTPResponse(status=404)

    items = filedb.get_items()
    return HTTPResponse(body=json.dumps(items), content_type='application/json')

def initdb(catalog_file):
    """ Initializes the database """
    global filedb   # pylint: disable=W0601,C0103
    filedb = FileDB(catalog_file)

if __name__ == '__main__':
    initdb(CATALOG_FILE)
    run(app, host='0.0.0.0', port=8123)
