#!/usr/bin/env python3

import email_sender
import dbconnconfig
import restclientutility

cursor = dbconnconfig.connection.cursor()

queryFile = open("queryfile", 'r')
queryString = queryFile.read()
queryFile.close()

claimsSuspended = ""
for row in cursor.execute(queryString):
    claimsSuspended = claimsSuspended + str(row[1]) + ","
print(claimsSuspended)
claimsSuspended = claimsSuspended.split(",")
print(str(claimsSuspended))

email_sender.emailutility(str(claimsSuspended))

headers = {
        'RequestCorrelationId': '123345566891_SCR_TEST',
        'systemofcall': 'workaroundscr'
    }

restclientutility.callrestendpoint("GET", "https://localhost:8080/uaa/user", None, headers)
