## Setup

#### Setting up the docker container 
This is used for local dev
```
docker run -e MYSQL_ROOT_PASSWORD=<password> -d -p 3306:3306 mysql:5.7.13
mysql -hlocalhost --protocol=TCP -uroot -p
```

#### To connect to the mysql database

`mysql -hlocalhost --protocol=tcp -u root  -p`

in order to run setup.sql, use the following command

`mysql -hlocalhost --protocol=tcp -u root  -p < setup.sql`

#### Set up virtualenv
`~ virtualenv venv`

`mysql -hlocalhost --protocol=tcp -u root  -p < setup.sql`

#### Set up virtualenv
`~ virtualenv venv`

#### Install dependencies
```
pip3 install mysqlclient==1.4.2
pip3 install docopt==0.6.2
```

#### Environmental Variables Needed
```
~ export DB_NAME=locator
~ export DB_HOST=<host>
~ export DB_USER=<user>
~ export DB_PASS=<password> 
```

#### Load csv into database
```
./convert_csv.py
```

## Example
Help
```
~ ./find_store.py -h
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
```
Find by address

```
~ ./find_store.py --address "5537 W Broadway Ave" --output json
[{'store_name': 'Crystal', 'store_location': 'SWC Broadway & Bass Lake Rd', 'address': '5537 W Broadway Ave', 'city': 'Crystal', 'state': 'MN', 'zip_code': '55428-3507', 'start_z
ip': 55428, 'end_zip': 53507, 'latitude': '45.0521539', 'longitude': '-93.364854', 'county': 'Hennepin County'}]
```

#### Assumptions:


#### Assumptions:
I worked on the assumption that all the locations I needed were located in the csv file.  As I thought about this
problem more, finding a nearby location based on a zip may be harder than I previously thought without a third party
tool or a separate implementation of a project.  Initially, I thought that I can create a database with a start and 
end zip range to filter a nearby location based on a zip input.  Maybe I need to utilize the lat and long location.

More business requirements gathering is needed.

Need to do:
1) More functionality, locate based on zip code ranges
2) More tests
3) Utilize third party tools to map out the closest locations based on lat and long values
4) Package up tool with setup.py
5) pep8 compliance
6) set up dependencies

