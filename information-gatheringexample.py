# <<import json
import socket
import requests
import sys
# host = input("Enter a hostname or IP address: ")
if(len(sys.argv) < 2):
    print("Usage of this command"
          "    info <url/domain>")
    sys.exit(1)

try:
        print(sys.argv)
        ip_address = socket.gethostbyname(sys.argv[1])
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