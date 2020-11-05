#========================#
# EEE3096 Mini-Project A #
# HRRHAN002 & TSHWAN006  #
# Nov 2020               #
#========================#

# Imports
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import ES2EEPROMUtils
import busio
import digitalio
import board
import threading
import os
from time import time
from datetime import datetime

# Global variables
chan = None # SPI channel
adc_thread = None # thread for the ADC reading function
temp = None # temperature value read from ADC

# Pins

# Setup peripherals (ADC, EEPROM, buttons)
def setup():
    global chan
    
    # Setup ADC
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI) # create the spi bus
    cs = digitalio.DigitalInOut(board.D5) # create the cs (chip select)
    mcp = MCP.MCP3008(spi, cs) # create the mcp object
    chan = AnalogIn(mcp, MCP.P1) # create an analog input channel on pin 1

    # Setup EEPROM
    eeprom = ES2EEPROMUtils.ES2EEPROM()

# Get reading from ADC, convert to temperature, call print_log (threaded)
def read_temp():
    global chan, thread, temp
    
    adc_thread = threading.Timer(5, read_temp) # execute every <interval> seconds
    adc_thread.daemon = True # Stop thread if program stops
    adc_thread.start()
    
    # Calculate temp
    # From datasheet: Vout = Tc * Ta + V0
    # => Ta = (Vout - V0) / Tc
    Tc = 10.0 # temp coeff from datasheet
    V0 = 0.5 # [V] Vout at T=0C from datasheet
    temp = (chan.voltage - V0)/Tc
    
    print_log()

# Store latest log entry in EEPROM (& ensure only 20 stored)
def store_log(time, systime, temp):
    # time: time of day in milliseconds (int)
    # systime: system timer - time since start of logging in milliseconds (int)
    # temp: temperature value (int)
    # -
    # Each item of data will be stored in a block
    # So the logs are stored consecutively, 3 blocks each
    # So the first index for time will be 1, last will be 58
    # first for temp is 3, last 60
    # -
    # The first block stores block index to put the next log at.
    # -
    
    # Read first block (1st reg) to get index:
    idx = eeprom.read_byte(0) # read reg
    if idx<1 or idx>58: # out of bounds
        idx = 1 # start at the start (wrap if idx reached the end)
    
    # Write data
    # time
    eeprom.write_block(idx, time)
    idx += 1
    # systime
    eeprom.write_block(idx, systime)
    idx += 1
    # temp
    eeprom.write_block(idx, temp)
    idx += 1
    
    # Write updated idx back
    eeprom.write_byte(0,idx)

# Display the latest log entry of temperature data
def print_log():
    pass

# Display column headings
def print_head():
    pass

# Get current time in form [hh,mm,ss]
def time_now():
    time = datetime.now()
    return [time.hour, time.minute, time.second]

# Convert time as [hh,mm,ss] to milliseconds
def time_to_ms(tm):
    return 3600000*tm[0] + 60000*tm[1] + 1000*tm[2]

# Convert time in milliseconds to a list [hh,mm,ss]
def ms_to_time(ms):
    return [(ms/3600000)%24, (ms/60000)%60, (ms/1000)%60]

# Enable/disable sampling (button callback)
def toggle_sampling():
    pass

# Clear console and print stop logging message
def clear_log():
    pass

# Clear stored logs in EEPROM
def clear_mem():
    eeprom.clear(240) # clear 60*4 registers

# Main
if __name__ == "__main__":
    try:

    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()

