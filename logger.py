#========================#
# EEE3096 Mini-Project A #
# HRRHAN002 & TSHWAN006  #
# Nov 2020               #
#========================#

# Imports

# Global variables

# Pins

# Setup peripherals (ADC, EEPROM, buttons)
def setup():
    pass

# Get reading from ADC and convert to temperature (threaded)
def read_temp():
    pass

# Store latest log entry in EEPROM (& ensure only 20 stored)
def store_log():
    pass

# Display the latest log entry of temperature data
def print_log():
    pass

# Display column headings
def print_head():
    pass

# Toggle sampling rate (button callback)
def toggle_sample_rate():
    pass

# Enable/disable sampling (button callback)
def toggle_sampling():

# Load log entries from EEPROM
def load_log():
    pass

# Clear stored logs in EEPROM
def clear_log():
    pass

# Main
if __name__ == "__main__":
    try:

    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()

