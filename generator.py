import json
import random

data = {f"Server{i}":random.randint(1, 100) for i in range(7)}

with open("/var/www/html/data.json", "w") as file:
	json.dump(data, file, indent=4)

