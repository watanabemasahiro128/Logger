import json
import requests

localhost_url = "http://localhost/"

if __name__ == "__main__":
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    data = json.dumps({"command": "pressure"})
    pressure = requests.post(localhost_url, headers=headers, data=data).json()["result"]
    print("Pressure :", pressure)