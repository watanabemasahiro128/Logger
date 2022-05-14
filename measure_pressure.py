import json
import requests

LOCALHOST_URL = "http://localhost/"

if __name__ == "__main__":
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    data = json.dumps({"command": "pressure"})
    pressure = requests.post(LOCALHOST_URL, headers=headers, data=data).json()["result"]
    print("Pressure :", pressure)
