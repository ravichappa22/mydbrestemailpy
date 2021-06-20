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
        response = requests.put(urltocall, data=data, headers=headers)
        print(response)

callrestendpoint("PUT", "http://localhost:8080/api/bycount/2000", None, None)


