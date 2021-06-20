import restoauthclient
import requests

def callrestendpoint(reqmethod, urltocall, data, headers):
    response = ""
    if reqmethod == "GET":
        print("GET for " + reqmethod)

    elif reqmethod == "POST":
        print("POST")
    elif reqmethod == "PUT":
        print("PUT")
        access_token = restoauthclient.preparetoken()

        finalheaders = {
        'Authorization': "Bearer " + str(access_token),
        'Content-Type': 'application/json'
    }
        finalheaders.update(headers)

        response = requests.put(urltocall, data=data, headers=finalheaders)
        print(response)
        return response




