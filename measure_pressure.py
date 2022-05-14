import json
import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv
import sentry_sdk

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(verbose=True, dotenv_path=dotenv_path)
SENTRY_DSN = os.environ.get("SENTRY_DSN")
LOCALHOST_URL = "http://localhost/"

sentry_sdk.init(SENTRY_DSN, traces_sample_rate=1.0)

if __name__ == "__main__":
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    data = json.dumps({"command": "pressure"})
    pressure = requests.post(LOCALHOST_URL, headers=headers, data=data).json()["result"]
    print("Pressure :", pressure)
