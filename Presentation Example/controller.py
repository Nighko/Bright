from voice_engine import ve
from internet_test import ping
internet_on = ping()
print("Booted, awaiting user input")
hotword = ve(False, internet_on)

print ("Recognised: " + hotword)
#if hotword == "hey illuminate" :
#    print("Hotword Detected")
#else:
#    print("Not Hotword D: it thinks you said: " + hotword)
input()
