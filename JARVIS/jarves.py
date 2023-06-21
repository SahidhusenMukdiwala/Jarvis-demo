from typing import Text
from urllib.parse import quote
import pyttsx3

from pywhatkit.misc import playonyt, search
import speech_recognition as sr
import datetime
from playsound import playsound
from googletrans import Translator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import wikipedia
import webbrowser
import requests
import os
import pyjokes
import pywhatkit
import random
import cv2
import webbrowser as web

# import MyAlarm

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning!')

    elif hour >= 12 and hour < 17:
        speak('Good afternoon!')

    elif hour >=17 and hour < 19:
        speak('Good evening!')

    else:
        speak('Good night!')

def userName():
    speak('Hello!! I am jarvis please tell me how may i help you')

def SpeedTest():
    import speedtest
    speak('Checking speed....')
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown =int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)
    if 'uploading' in query:
        speak(f'Uploading speed is {correctUpload} mbp s')
        
    elif 'downloading' in query:
        speak(f'The Downloading speed is {correctDown} mbp s')


    elif 'internet speed' in query:
        speak(f'The Downloading speed is {correctDown} and The uploading speed is {correctUpload}mbp s')

def Whatsapp():
    speak('Tell me the name Of the person!')
    name = takeCommand()

    if 'moazzam' in query:
        speak('Tell Me the messege!')
        msg = takeCommand()
        speak('Tell me the time sir')
        speak('Time in hour')
        hour = int(takeCommand())
        speak('Time in Minutes!')
        min = int(takeCommand())
        pywhatkit.sendwhatmsg('+91 96387 56693', msg, hour, min, 20)
        speak('Ok sir, Sending Whatsapp messege!')

def music():
    speak('Tell me the name of the song')
    musicName = takeCommand()

    if 'mann bhariya' in musicName:
        os.startfile('D:\\favorite songs2')

    else:
        pywhatkit.playonyt(musicName)
        speak('Your song has been started!, Enjoy sir!')

        # def OpenApps():
        #     speak('Ok sir, please wait a moment')

def takeCommand():
    # it takes microphone input from the user returns string output
    r = sr.Recognizer()
    with sr.Microphone()() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        speak('Please say something ......')
        return 'None'

    return query.lower()

def TakeHindi():
    # it takes microphone input from the user com
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='hi')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        # speak('Say that again please....')
        return 'None'

    return query.lower()

def Tran():
    speak('Tell me the line!')
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)

def my_location():

    loc = 'https://www.google.com/maps/place/Gujarat/@22.4064165,69.0747339,7z/data=!3m1!4b1!4m5!3m4!1s0x3959051f5f0ef795:0x861bd887ed54522e!8m2!3d22.258652!4d71.1923805'
    speak('checking......')
    web.open(loc)
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https//get.geojs.io/v1/ip/geo' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d  = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f'sir,Are you in {state,country}')


def Temperature():
    speak('In which city sir!')   
    city = takeCommand().lower()
    print(city)
    # search = f'Temperature in {city}'
    url = f'https://www.google.com/search?q={search}'
    r = requests.get(url)
    data = BeautifulSoup(r.text,'html.parser')
    temperature = data.find('div',class_=' BNeawe').text
    speak(f'The Temperature Outside Is {temperature}celcius')
    
Hello = ('how are you jarvis')

reply_Hello = ('Hello sir,Nice to meet you agin ')

bye = ('you need a break')

reply_bye = ('bye sir')

# how_are_you = ('How are you jarvis')

# reply_how = ('I am fine sir','How are you sir')

def chatterbot(Text):
    Text = str(Text)

    for word in Text.split():
        if word in Hello:
            reply = random.choice(reply_Hello)
            return reply
        elif word in bye:
            reply = random.choice(reply_bye)
            return reply

        # elif word in how_are_you:
        #     reply = random.choice(reply_how)
        #     return reply

if __name__ == '__main__':
    wishMe()
    userName()
    while True:
        # if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            speak('Acording to Wikipidia')
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('Sir, What should i search on google')
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
 
        elif 'play songs on youtube' in query:
            pywhatkit.playonyt('Dil diya gallan')

        # elif 'play music' in query:
        #     music_dir = 'D:\\favorite songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'music' in query:
            music()
            break

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir , the time is {strtime}')

        elif 'how are you jarvis' in query:
            speak('i am fine sir, thank you')
            speak('How are you, sir')

        elif 'you need a break' in query:
            speak('Ok sir,You can call me Anytime!')
            # speak('just say Wakeup jarvis')
            break

        elif 'fine' in query or 'good' in query:
            speak('Its good to know that your fine')

        # elif 'change my name to' in query:
        #     query = query.replace('Change my name to', 'siri')
        #     assname = query
        #     speak(assname)

        elif 'change name' in query:
            # query = query.replace('Change my name to', 'siri')
            speak('What would you call me, sir')
            assname = takeCommand()
            speak('thanks for naming me,it is really funny name')

        # elif 'gandu' in query:
            # speak('tu gandu tera baap gandu,tera dada gandu,gali kisko di jat ke baal')

        elif 'temperature' in query:
            Temperature()

        # elif 'who is my company friend' in query:
        #     speak('atif,moazzam,rehan,shadab,sahaf,zahuruddin,saamir,samir,hasnain,raiyyan')

        elif "what's your name" in query or 'what is your name' in query:
            speak('my friends call me jarvis ')

        elif 'will you be my bf' in query or 'will you be my gf ' in query:
            speak('i am not sure about, may be you should give me some time')

        elif 'who made you ' in query or "who create's you" in query:
            speak('I have been created by sahid.')

        elif 'reason for you' in query or 'why are you created' in query:
            speak('I was created as a minor project by mr.sahid husen')

        elif 'sorry' in query:
            speak('sorry foziya , from my master sahid ')

        elif 'translator' in query:
            Tran()

        elif 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'internet speed' in query:
            SpeedTest()

        elif 'how to' in query:

            speak('Getting Data From the Internet!')
            a = query.replace('jarvis','')
            max_result = 1
            how_to_func = search_wikihow(a,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'find location' in query:
            from Feature import my_location
            my_location()

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'alarm' in query:
            speak('Enter the time!')
            time = input(':Enter the time: ')

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime('%H:%M:%S')

                if now == time:
                    speak('Time to wake up sir!')
                    playsound('Tera Yaar Hoon Main.mp3')
                    speak('Alarm closed')

                elif now>time:
                    break
        
        # elif 'set alarm' in query:
        #     speak('Tell me the time to set alarm.set alaem to 5.30 am')
        #     tt  = takeCommand()
        #     tt = tt.replace('set alarm to','')
        #     tt = tt.replace('.','')
        #     tt = tt.upper()
        #     import MyAlarm
        #     MyAlarm.alarm(tt)

        elif 'WhatsApp messege' in query:
            Whatsapp()
            
        elif 'what are you doing' in query:
            speak('i am interact with you sir .... ')

        elif 'Exit' in query:
                speak('That was great talk . See you soon sir . ')
                exit()
