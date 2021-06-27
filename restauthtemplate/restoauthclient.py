#!/usr/bin/env python3

import os
import requests
import base64
import json

systemUser = os.getenv('SYSTEM_USER')
systemPassword = os.getenv('SYSTEM_PASSWORD')
clientId = os.getenv('CLIENT_ID')
clientSecret = os.getenv('CLIENT_SECRET')
tokenUrl = os.getenv('REST_AUTH_BASEURI')
tokenFullPathUrl = str(tokenUrl) + "/uaa/oauth/token"

strToEndcode = str(clientId) + ":" + str(clientSecret)
message_bytes = strToEndcode.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')


def preparetoken():
    payload = "grant_type=password&username=" + str(systemUser) + "&password=" + str(systemPassword)
    headers = {
        'Authorization': "Basic " + str(base64_message),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    cafile = 'certificate.pem'  # location of cafile

    response = requests.post(tokenFullPathUrl, data=payload, headers=headers, verify=False)

    access_token = json.loads(response.text)["access_token"]

    return access_token
