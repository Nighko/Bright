# Imports start
import datetime
from lib2to3.pgen2.token import PERCENT
from google import google
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import alsaaudio
from tts import tts_engine as ttse


# Imports finish
# Early Stages
def google(search_term):
    counter = 0
    search_terms = search_term.split()
    if "google" in search_terms:
        del search_terms[0:1]
    if "search for" in search_terms:
        del search_terms[0:2]
    search_terms = ' '.join(search_terms)
    # 
    num_page = 1
    search_results = google.search(search_terms, num_page)
    for result in search_results:
        if counter == 4:
            break
        counter = counter + 1
        ttse("f", "Title " + result.name)

        
class volume():
    m = alsaaudio.Mixer()

    def up(self, percentage):
        current_volume = self.m.getvolume()
        print("Increase Volume by ", percentage)
        self.m.setvolume(current_volume + percentage)

    def down(self, percentage):
        current_volume = self.m.getvolume()
        print("Decrease Volume by ", percentage)
        self.m.setvolume(current_volume - percentage)

    def set(self, value):
        print("Volume set to: ", value)

    def get(self):
        current_volume = self.m.getvolume()
        return current_volume
    
