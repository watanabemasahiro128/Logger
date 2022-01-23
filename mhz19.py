import mh_z19

def measure_co2concentration():
    try:
        return mh_z19.read(serial_console_untouched=True)["co2"]
    except OSError:
        return -1
