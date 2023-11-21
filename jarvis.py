import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import pyjokes


def sptext():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio= recognizer.listen(source)
    try:
        print("recognizing...")
        data=recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Not Understand") 


def speechtx():
    engine = pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate= engine.getProperty('rate')
    engine.setProperty('rate',140)
    engine.say()
    engine.runAndWait() 

if __name__ == '__main__':
    while True:
        data1 = sptext().lower()
        if 'your name' in data1:
            name= "my name is jarvis"
            speechtx(name)

        elif 'old are you' in data1:
            age= "I am 12 years old"
            speechtx(age)
        
        elif 'time' in data1:
            time =datetime.datetime.now().strftime("%I %M %p")
            speechtx(time)
        
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")


        elif 'joke' in data1:
            jokes_1 = pyjokes.get_joke(language="en",category='neutral')
            speechtx(jokes_1)

        elif 'playsong' in data1:
            add= "/home/tarunsharma"#path to music folder
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong))

        elif "exit" in data1:
            speechtx("thank you")
            break