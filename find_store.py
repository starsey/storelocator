#!/usr/bin/env python3
"""

find_store will locate the nearest store (as the vrow flies) from
  store-locations.csv, print the matching store address, as well as
  the distance to that store.

Usage: ./find_store.py [options] [LOCATION] [OUTPUT]...

Arguments:
  LOCATION         The location input
  OUTPUT           The format of the output

Options:
  --zip            Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address        Find nearest store to this address. If there are multiple best-matches, return the first.
  --units          Display units in miles or kilometers [default: mi]
  --output         Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

Example:
  find_store --address "1770 Union St, San Francisco, CA 94123"
  find_store --zip 94115 --units km
"""
from docopt import docopt
from os import getenv
import MySQLdb

class Store:
    """
    Arbitrary Store Class
    """
    def __init__(self):
        self.db = MySQLdb.connect(host=getenv('DB_HOST'),
                                  user=getenv('DB_USER'),
                                  passwd=getenv('DB_PASS'),
                                  db=getenv('DB_NAME'))
        self.cursor = self.db.cursor()
        self.row_headers = None

    def get_headers(self):
        self.row_headers = [x[0] for x in self.cursor.description]
        return self.row_headers

    def find_location_by_address(self, address, output='text'):
        query = "SELECT * FROM location WHERE address='{}'".format(address)
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        if output == 'json':
            return self.format_json(results)
        else:
            return self.format_text(results)

    def format_json(self, results):
        self.get_headers()
        json_data=[]
        for r in results:
            json_data.append(dict(zip(self.row_headers, r)))
        return json_data

    def format_text(self, results):
        return results[0][0:6]


if __name__ == '__main__':
    arguments = docopt(__doc__)
    find_store = Store()
    try:
        output = arguments['OUTPUT'][0]
    except IndexError:
        output = 'text'
    if arguments["--address"]:
        addr = (arguments['LOCATION'])
        print(find_store.find_location_by_address(addr, output))
