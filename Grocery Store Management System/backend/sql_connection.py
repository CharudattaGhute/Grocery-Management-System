import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='your_username', password='your_password',host="127.0.0.1", database='grocery_store')

  return __cnx

