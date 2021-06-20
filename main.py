#!/usr/bin/env python3

import email_sender
import dbconnconfig

cursor = dbconnconfig.connection.cursor()

queryFile = open("claimsFile", 'r')
queryString = queryFile.read()
queryFile.close()

claimsSuspended = ""
for row in cursor.execute(queryString):
    claimsSuspended = claimsSuspended + str(row[1]) + ","
print(claimsSuspended)
claimsSuspended = claimsSuspended.split(",")
print(str(claimsSuspended))

email_sender.emailutility(str(claimsSuspended))
