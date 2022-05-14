import json
import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv
import mhz19

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(verbose=True, dotenv_path=dotenv_path)
GAS_URL = os.environ.get("GAS_URL")
LOCALHOST_URL = "http://localhost/"

if __name__ == "__main__":
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    data = json.dumps({"command": "temperature"})
    temperature = requests.post(LOCALHOST_URL, headers=headers, data=data).json()["result"]
    print("Temperature :", temperature)
    data = json.dumps({"command": "pressure"})
    pressure = requests.post(LOCALHOST_URL, headers=headers, data=data).json()["result"]
    print("Pressure :", pressure)
    data = json.dumps({"command": "humidity"})
    humidity = requests.post(LOCALHOST_URL, headers=headers, data=data).json()["result"]
    print("Humidity :", humidity)
    data = json.dumps({"command": "illuminance"})
    illuminance = requests.post(LOCALHOST_URL, headers=headers, data=data).json()["result"]
    print("Illuminance :", illuminance)
    co2 = mhz19.measure_co2concentration()
    print("CO2 :", co2)

    data = json.dumps({"Temperature": temperature, "Pressure": pressure, "Humidity": humidity, "Illuminance": illuminance, "CO2": co2})
    status = requests.post(GAS_URL, headers=headers, data=data).json()
    print(status)
