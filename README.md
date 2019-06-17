###Setting up the docker container

`docker run -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:5.7.13
mysql -hlocalhost --protocol=TCP -uroot -p1234`

###To connect to the mysql database

`mysql -hlocalhost --protocol=tcp -u root  -p`

### set up virtualenv
`~ virtualenv venv`

`pip3 install mysqlclient`

https://pypi.org/project/mysqlclient/


pip install pymysql
pip install mysqlclient



https://gist.github.com/valsiebs/8531809

pip install docopt==0.6.2

Assumptions:


Need to do:
1) More functionality
2) More tests
3) utilize third party tools to map out the closest locations based on lat and long values
4) package up tool with setup.py
5) pep8 compliance

