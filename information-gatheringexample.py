# <<import json
import socket
import requests
import sys
# host = input("Enter a hostname or IP address: ")

try:
        print(host)
        ip_address = socket.gethostbyname(host)
        rep_two = requests.get("https://ipinfo.io/"+ip_address+"/json")
        # print(f'Scanning the IP address: {ip_address}')

        resp = json.loads(rep_two.text)
        print("Domain         : "+resp["ip"])
        print("Location       : "+resp["loc"])
        print("Region         : "+resp["region"])
        print("City           : " + resp["city"])
        print("Country        : "+resp["country"])
        print("Organisation   : " + resp["org"])
        print()
except socket.gaierror as e:
        print("Error: Invalid hostname or IP address provided.") 
