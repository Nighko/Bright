# Import custom functions
from voice_engine import ve, calib
from tts import tts_engine as ttse
from internet_test import ping
# Import installed libraries
import csv
# Check for internet connection. Use WIT.AI if you have one and use
# PocketSphinx if offline.
internet_on = ping()
with open('preferences.csv') as  csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        g = row[0]
calib()
ttse(g, "Bright is online")
while(True):
    ttse(g, "Awaiting user input")
    recog = ve(False, internet_on)
    ttse(g, "Recognised: " + recog)
    #if hotword == "hey illuminate" :
    #    print("Hotword Detected")
    #else:
    #    print("Not Hotword D: it thinks you said: " + hotword)
