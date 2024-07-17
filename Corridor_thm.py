import hashlib
import requests
url = input("Enter the url : ")
objects = []
for i in range(0,101):
	hashing = hashlib.md5(str(i).encode())
	md5 = hashing.hexdigest()
	objects.append(md5)
try:
	for payload in objects:
		response = requests.get(url+payload)
		if response.status_code==200: print(f"Response : {response.status_code},\t ==> {url}/{payload} ")
except KeyboardInterrupt: 
	print("Finished !!!")