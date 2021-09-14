import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print("Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print("Error: '{err}'")
def init_database(connection):
    cursor = connection.cursor()
    try:
        query="CREATE DATABASE IF NOT EXISTS twilioTextBookBalancer;"
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print("Error during database initialization, could not create db: '{err}'")


def init_table(connection):
    cursor = connection.cursor()
    try:
        query="CREATE DATABASE IF NOT EXISTS twilioTextBookBalancer;"
        cursor.execute(query)

        query="USE twilioTextBookBalancer;"
        cursor.execute(query)

        query="CREATE TABLE IF NOT EXISTS messages (id INT NOT NULL AUTO_INCREMENT, fromNum CHAR(30) NOT NULL, cost DECIMAL(18,2) NOT NULL, details VARCHAR(250), dateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (id));"
        cursor.execute(query)
        print("Table created successfully")
    except Error as err:
        print("Error during table initialization, could not create table: '{err}'")

def init_table2(connection):
    #init two tables, a user table and a message table
    cursor = connection.cursor()
    try:
        query="CREATE DATABASE IF NOT EXISTS twilioTextBookBalancer;"
        cursor.execute(query)

        query="USE twilioTextBookBalancer;"
        cursor.execute(query)

        query="CREATE TABLE IF NOT EXISTS users(userID INT NOT NULL AUTO_INCREMENT, userNumber CHAR(30) NOT NULL UNIQUE,startDate DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, active BOOLEAN NOT NULL DEFAULT 1, PRIMARY KEY(userID));"
        cursor.execute(query)
        query="CREATE TABLE IF NOT EXISTS messages (id INT NOT NULL AUTO_INCREMENT, fromNum CHAR(30) NOT NULL, cost DECIMAL(18,2) NOT NULL, details VARCHAR(250), dateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (id), FOREIGN KEY(fromNum) REFERENCES users(userNumber) ON DELETE CASCADE ON UPDATE CASCADE);"
        cursor.execute(query)
        print("Table created successfully")
    except Error as err:
        print("Error during table initialization, could not create table: '{err}'")






