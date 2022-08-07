from dataclasses import dataclass
import re
from sqlite3 import connect
import mysql.connector

from faker import Faker
fake = Faker()



# connection = mysql.connector.connect(host='localhost',database='learning',user='root')

# cursor = connection.cursor()
# cursor.execute("select * from Persons limit 10;")
# cursor.execute("insert into Persons(LastName,FirstName,Address,City) values ('Krasivik','Mujcina','Urdak 10','Hell')")
# cursor.execute("select count(*) from Persons")
# connection.commit()
# print(cursor.fetchone())
# cursor.close()
# connection.close()

def makeConnection(database):
    return mysql.connector.connect(host='localhost',database=database,user='root')

def fillTable(tableName):
    connection = makeConnection("learning")
    cursor = connection.cursor()
    cursor.execute("insert into {}(LastName,FirstName,Address,City) values ('{}','{}','{}','{}')".format(tableName,fake.last_name(),fake.first_name(),fake.address(),fake.city()))
    connection.commit()
    cursor.close()
    connection.close()

def getCountOfCells(tableName):
    connection = makeConnection("learning")
    cursor = connection.cursor()
    cursor.execute("select count(*) from {}".format(tableName))
    response = cursor.fetchone()
    cursor.close()
    connection.close()
    return response[0]



print("hello")
fillTable("Persons")
getCountOfCells("Persons")

for i in range(getCountOfCells("Persons")):
    fillTable("Persons3")