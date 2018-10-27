# Text to speech class file
# (Python's class system is a little different to what I'm used to, I may try to use it later)
# USAGE:
# from tts import tts_engine as ttse
# 
# ttse(m, "This is an example")

def tts_engine(gender, text):
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if gender == 'm':
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    elif gender == 'f':
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        