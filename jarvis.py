from typing import Mapping
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #already built-in module
import wikipedia #pip install wikipedia
import webbrowser #already built-in module
import os #already built-in module
import random #already built-in module

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    if(hour>=12 and hour<18):
        speak("Good Afternoon")
    if(hour>18):
        speak("Good Evening")
    
    speak("Hello I am Jarvis..Please tell me how may i help you?")

def takeCommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User Said:",query)
    
    except Exception as e:
        #print(e)
        print("Say that again please..")
        return "None"
    return query  


if __name__== "__main__":
    wishMe()
    while(True):
        query=takeCommand().lower()
        #logic for executing tasks according to query
        if 'wikipedia' in query:
            speak("searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
             webbrowser.open("google.com")
        elif 'open youtube' in query:
             webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
             music_dir='H:\\Songs'
             songs=os.listdir(music_dir)
             print(songs)
             list=[0,1,2,3,4,5]
             i=random.choice(list)
             print("i=",i)
             os.startfile(os.path.join(music_dir,songs[i]))
        elif 'the time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Madam,Now time is {strTime}")
        
        elif 'open vs code' in query:
              codePath="C:\\Users\\lapcom solution\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codePath)

        elif 'open pycharm' in query:
              codePath1="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
              os.startfile(codePath1)

        elif 'email to Tejal' in query:
                try:
                    speak('tell me what should I say?')
                    content=takeCommand()
                    to=tejal.narkhede2406@gmail.com
                    sendEmail(to,content)
                    speak("Email Sent Successfully!")
                except Exception as e:
                    print(e)
                    speak("Sorry Tejal...I am not able to send this email..!")
        elif 'quit' in query:
            exit()
            