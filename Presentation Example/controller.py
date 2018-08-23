# Import custom functions
from voice_engine import ve, calib
from internet_test import ping
# Import installed libraries
import csv
import os
def ttse(text):
	text2 = text
	os.system("espeak -v en-us '" + text2 + "' 2>/dev/null")
# PocketSphinx if offline.
internet_on = ping()
with open('preferences.csv') as  csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        g = row[0]
calib()
while(True):
    ttse("Awaiting user input")
    print("Awaiting user input")
    recog = ve(False, internet_on)
    ttse("Recognised: " + recog)
    print("Recognised: " + recog)
    #if hotword == "hey illuminate" :
    #    print("Hotword Detected")
    #else:
    #    print("Not Hotword D: it thinks you said: " + hotword)
input()
