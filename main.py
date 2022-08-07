from dataclasses import dataclass
import re
from sqlite3 import connect
import mysql.connector

from faker import Faker
fake = Faker()

def makeConnection(database):
    return mysql.connector.connect(host='localhost',database=database,user='root')

def createTable(name):
    connection = makeConnection("learning")
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS {} (
    PersonID int auto_increment primary key,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
    );""".format(name))
    connection.commit()
    cursor.close()
    connection.close()
    return name

def fillTable(tableName,length):
    connection = makeConnection("learning")
    cursor = connection.cursor()
    requestInsert = "insert into {}(LastName,FirstName,Address,City) values (%s,%s,%s,%s);".format(tableName)
    requestValues = []
    for i in range(length):
        if i%1000==0:
            print("Prepare in {}. {} from {}".format(tableName,i,length))
        requestValues.append((fake.last_name(),fake.first_name(),fake.address(),fake.city()))
    print("Request...")
    cursor.executemany(requestInsert,requestValues)
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

length = 10000

nameOfFirstTable = createTable("Persons")

fillTable(nameOfFirstTable,length)


for i in range(10):
    i+=1
    fillTable(createTable(nameOfFirstTable+"{}".format(i)),length)