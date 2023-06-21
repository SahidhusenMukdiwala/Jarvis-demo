from math import trunc
import os
import speech_recognition as sr


def takeCommand():

    # it takes microphone input from the user returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        # speak('Say that again please....')

        # return query.lower()

        while True:

            wake_Up = takeCommand()

            if 'wake up' in wake_Up:
                os.startfile('D:\\JARVIS')

            else:
                print('Nothing......')