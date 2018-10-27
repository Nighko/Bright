"""

Bright - Voice Assistant made by Nighko from Unamridge

Repository: https://repo.unamridge.org/nighko/Bright
Wiki: https://repo.unamridge.org/nighko/Bright/wiki
Email: nighko@unamridge.org

If you find an issue, please post it on the repository issues section!

"""

# Import custom functions
import csv

from actions import *
from internet_test import ping
from tts import tts_engine as ttse
from voice_engine import ve, calib

# Import installed libraries
# Check for internet connection. Use WIT.AI if you have one and use
# PocketSphinx if offline.
internet_on = ping()
with open('preferences.csv') as  csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        g = row[0]
calib()
ttse(g, "Bright is online")
while(True):
    volume.up(percentage=75)
    print(volume.get())
    volume.down(percentage=75)
    print(volume.get())
    
"""    ttse(g, "Awaiting user input")
    print("Awaiting user input")
    recog = input('Speak:')  # ve(False, internet_on)
    ttse(g, "Recognised: " + recog)
    print("Recognised: " + recog)"""
input()
