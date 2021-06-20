import restoauthclient
import requests

def callrestendpoint(reqmethod, urltocall, data, headers):
    response = ""
    access_token = restoauthclient.preparetoken()
    finalheaders = {
        'Authorization': "Bearer " + str(access_token),
        'Content-Type': 'application/json'
    }
    finalheaders.update(headers)

    if reqmethod == "GET":
        print("GET for " + reqmethod)
        response = requests.get(urltocall, data=data, headers=finalheaders, verify=False)
    elif reqmethod == "POST":
        print("POST")
        response = requests.post(urltocall, data=data, headers=finalheaders, verify=False)
    elif reqmethod == "PUT":
        print("PUT")
        response = requests.put(urltocall, data=data, headers=finalheaders, verify=False)

    print("status code = " + str(response.status_code) + " response body = " + str(response.text))
    return response




