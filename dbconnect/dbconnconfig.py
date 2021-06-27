#!/usr/bin/env python3

import os
import cx_Oracle
username = os.getenv('ORACLE_USERNAME')
password = os.getenv('ORACLE_PASSWORD')
host = os.getenv('ORACLE_HOST')
port = os.getenv('ORACLE_PORT')
service = os.getenv('ORACLE_SVC_NAME')
dsn = host+":"+port+"/"+service

print(username)
print(password)
print(dsn)

cx_Oracle.init_oracle_client(lib_dir="/Users/rchappa1/Documents/Softwares/instantclient_19_8")

connection = cx_Oracle.connect(username,password,dsn)
print("connection made successfully")

