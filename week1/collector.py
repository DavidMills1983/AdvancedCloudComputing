import requests
import sys

url = sys.argv[1]

data = requests.get(url).json()

resource_dict = {"under":0, "over":0}


for (server, resource) in data.items():
	print(server, resource)
	if resource > 49:
		resource_dict["over"] += 1
	else:
		resource_dict["under"] += 1

print(resource_dict)




