#!/usr/bin/python3
import pymysql


def conecta():
    connection = pymysql.connect("localhost",  "root",  "root" ,"erpy");
    cursor = connection.cursor();
    return cursor

