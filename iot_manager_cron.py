import json
import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv
import sentry_sdk

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(verbose=True, dotenv_path=dotenv_path)
GAS_URL = os.environ.get("GAS_URL")
SENTRY_DSN = os.environ.get("SENTRY_DSN")
LOCALHOST_URL = "http://localhost/"

sentry_sdk.init(SENTRY_DSN, traces_sample_rate=1.0)

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
    data = json.dumps({"command": "co2"})
    co2 = requests.post(LOCALHOST_URL, headers=headers, data=data).json()["result"]
    print("CO2 :", co2)

    data = json.dumps({"Temperature": temperature, "Pressure": pressure, "Humidity": humidity, "Illuminance": illuminance, "CO2": co2})
    response = requests.post(GAS_URL, headers=headers, data=data).json()
    print(response)
    if response["status"] == 1:
        sentry_sdk.set_level("info")
        sentry_sdk.capture_message(f"Status: {response['status']}")
    else:
        sentry_sdk.capture_exception(Exception(f"Status: {response}"))
