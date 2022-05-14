import mh_z19
import os
from os.path import join, dirname
from dotenv import load_dotenv
import sentry_sdk

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(verbose=True, dotenv_path=dotenv_path)
SENTRY_DSN = os.environ.get("SENTRY_DSN")

sentry_sdk.init(SENTRY_DSN, traces_sample_rate=1.0)

def measure_co2concentration():
    return mh_z19.read(serial_console_untouched=True)["co2"]
