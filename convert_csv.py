#!/usr/bin/env python3
from os import getenv
import csv
import MySQLdb
import sys

def csv_to_mysql():
    '''
    This function load a csv file to MySQL table
    '''
    try:
        mydb = MySQLdb.connect(host=getenv('DB_HOST'),
                               user=getenv('DB_USER'),
                               passwd=getenv('DB_PASS'),
                               db=getenv('DB_NAME'))
        cursor = mydb.cursor()
        with open('store-locations.csv') as csv_file:
            # skip the first line that defines the header for the csv
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            end_zip = 213
            for row in csv_reader:
                start_zip_str = row[5].split('-')[0].strip()
                start_zip = int(start_zip_str)

                try:
                    if start_zip_str[0] != '0':
                        end_zip = int(start_zip_str[0])*10000 + int(row[5].split('-')[1].strip())
                        print("end_zip: {}".format(end_zip))
                except:
                    end_zip = start_zip
                query = 'INSERT INTO location(' \
                      'store_name, store_location, address, city, state, zip_code, start_zip, end_zip, latitude, longitude, county )' \
                      ' VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(row[0], row[1], row[2], row[3], row[4],
                                                                          row[5], start_zip, end_zip, row[6], row[7], row[8])

                cursor.execute(query)
            mydb.commit()
            cursor.close()
            print("Done")
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

def main():
    csv_to_mysql()

if __name__ == "__main__":
    main()
