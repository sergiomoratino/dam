#!/usr/bin/python3

import pymysql

connection = pymysql.connect("localhost",  "root",  "root.4dec" ,"erpy");
cursor = connection.cursor();

sql_query = "SELECT VERSION()";

try :
    cursor.execute( sql_query );
    data = cursor.fetchone();
    print( "Database Version: %s" %data );
    
except Exception as e :
    print("Exception : ", e);
connection.close();