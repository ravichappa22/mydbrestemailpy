#!/usr/bin/env python3

import email_sender
import dbconnconfig
import restclientutility
import json

cursor = dbconnconfig.connection.cursor()

queryFile = open("queryfile", 'r')
query = queryFile.read()
queryFile.close()

claimsSuspended = ""

for row in cursor.execute(query):
    claimsSuspended = claimsSuspended + str(row[1]) + ","
    url = "http://localhost:8080/api/bycount/2".format(str(row[1]))
    querystring = {"clmDtCmplCheck": "false"}
    payload = json.dumps({"dedAggrIndicator": "Y"})
    headers = {
            'RequestCorrelationId': '123345566891_SCR_TEST',
            'systemofcall': 'workaroundscr'
        }
    restclientutility.callrestendpoint("PUT", url, data=payload, headers=headers,  parameters=querystring)

print(str(claimsSuspended))

email_sender.emailutility(str(claimsSuspended))