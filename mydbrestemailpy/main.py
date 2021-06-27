#!/usr/bin/env python3

import json
import os

from appliationconfig.configreaderutil import ReadProfile
from dbconnect import dbconnconfig
from emailutility import email_sender
from restauthtemplate import restclientutility


cursor = dbconnconfig.connection.cursor()

queryFile = open("../queryfile", 'r')
query = queryFile.read()
queryFile.close()

claimsSuspended = []
url = ReadProfile().readandfindconfig(os.getenv("PROFILE", "prod"), "suspendclaimurl")

for row in cursor.execute(query):
    claimsSuspended.append(str(row[0]))
    url = url.format(str(row[0]))
    querystring = {"clmDtCmplCheck": "false"}
    payload = json.dumps({"dedAggrIndicator": "Y"})
    headers = {
            'RequestCorrelationId': '123345566891_SCR_TEST',
            'systemofcall': 'workaroundscr'
        }
    restclientutility.callrestendpoint("PUT", url, data=payload, headers=headers, parameters=querystring)

print(claimsSuspended)

if len(claimsSuspended) > 0:
    email_sender.emailutility(str(claimsSuspended))
else:
    print("No Claims Today to Suspend , so no email")