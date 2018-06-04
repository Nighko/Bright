# Voice Engine class. ABSTRACT
def ve(dummy_engine, internet_on):

    import speech_recognition as sr
    r = sr.Recognizer()
    # Check for internet connection (If connected: Wit.AI/If not connected: PocketSphinx)
    # Get Audio
    with sr.Microphone() as source:
        print("Calibrating")
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        if internet_on == True:
            # Use Wit AI
            WIT_AI_KEY = "E7EQGHO4L2ZLAJCZF32UGNN3WA5ILCBW"
            try:
                user_input = r.recognize_wit(audio, key=WIT_AI_KEY)
            except sr.UnknownValueError:
                user_input= 0
        else:
                # Use PocketSphinx
            try:
                user_input=r.recognize_sphinx(audio)
            except sr.UnknownValueError:
                user_input= 0
    return user_input
