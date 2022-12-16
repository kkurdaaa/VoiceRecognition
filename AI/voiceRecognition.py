
import speech_recognition as sr #text to sound

import pyttsx3 #voice

import datetime

import wikipedia

import webbrowser

import os

import time

import subprocess

import wolframalpha

import json

import requests





print('Loading')



engine=pyttsx3.init('sapi5') #dangi kabrayakaya 

voices=engine.getProperty('voices')

engine.setProperty('voice','voices[0].id')#grri dang





def speak(text):

    engine.say(text)#har qsaki bka 

    engine.runAndWait()#rawasti u chawarey qsay tu bka



def wishMe():#method 

    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:

        speak("Hello,Good Morning")

        print("Hello,Good Morning")

    elif hour>=12 and hour<18:#else if (la python waha danusre)

        speak("Hello,Good Afternoon")

        print("Hello,Good Afternoon")

    else:

        speak("Hello,Good Evening")

        print("Hello,Good Evening")



def takeCommand():#comand i tu wardagri bzani ch darey 

    r=sr.Recognizer()#recognize dangt daka 

    with sr.Microphone() as source:#microphone esh pedaka 

        print("Listening...")

        audio=r.listen(source)#dangakay lera xazn daka 



        try:

            statement=r.recognize_google(audio,language='en-in')

            print(f"user said:{statement}\n")#f=function 


#try except lo awaya shtak logic nabi bas error nada 
        except Exception as e:

            speak("sorry, please say that again")

            return "None"

        return statement



speak("Loading")

wishMe()





if __name__=='__main__':#__ constructor class drust dakay lanaw class'akay xoy bakar daynyawa





    while True:#infinity loop

        speak("Tell me how can I help you?")

        statement = takeCommand().lower()#dakata small lower

        if statement==0:

            continue #wak switch esh daka 



        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:

            speak(' shutting down,Good bye')

            print(' shutting down,Good bye')

            break







        if 'wikipedia' in statement:

            speak('Searching Wikipedia...')

            statement =statement.replace("wikipedia", "")

            results = wikipedia.summary(statement, sentences=3)#har chand bu awanda xataya agar 5 bu 5 xati danusi

            speak("According to Wikipedia")

            print(results)

            speak(results)



        elif 'open youtube' in statement:

            webbrowser.open_new_tab("https://www.youtube.com")

            speak("youtube is open now")

            time.sleep(5)#qsat nakrd awish qsan naka hata 5 sanyay



        elif 'open google' in statement:

            webbrowser.open_new_tab("https://www.google.com")

            speak("Google chrome is open now")

            time.sleep(5)



        elif 'open gmail' in statement:

            webbrowser.open_new_tab("gmail.com")

            speak("Google Mail open now")

            time.sleep(5)



        elif "weather" in statement:

            api_key="8ef61edcf1c576d65d836254e11ea420" # api website'a datay weather't lo dayni

            base_url="https://api.openweathermap.org/data/2.5/weather?"

            speak("whats the city name")

            city_name=takeCommand()

            complete_url=base_url+"appid="+api_key+"&q="+city_name

            response = requests.get(complete_url)#request daneri lo webstite ba kaml parameter

            x=response.json()#javascript object notation lo a3lumat xazn krdnu garanawaya

            if x["cod"]!="404":

                y=x["main"]

                current_temperature = y["temp"]

                current_humidiy = y["humidity"]

                z = x["weather"]

                weather_description = z[0]["description"]

                speak(" Temperature in kelvin unit is " +

                      str(current_temperature) +

                      "\n humidity in percentage is " +

                      str(current_humidiy) +

                      "\n description  " +

                      str(weather_description))

                print(" Temperature in kelvin unit = " +

                      str(current_temperature) +

                      "\n humidity (in percentage) = " +

                      str(current_humidiy) +

                      "\n description = " +

                      str(weather_description))



            else:

                speak(" City Not Found ")







        elif 'time' in statement:

            strTime=datetime.datetime.now().strftime("%H:%M:%S")#hour minute second

            speak(f"the time is {strTime}")



        elif 'who are you' in statement or 'what can you do' in statement:

            speak('I am Student in Tishk university and this is my project')





        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:

            speak("I was built by Tara and talar")

            print("I was built by tara and talar")



        elif "open stackoverflow" in statement:#gawratrin question and answer'i programinga


            webbrowser.open_new_tab("https://stackoverflow.com/login")

            speak("Here is stackoverflow")



        elif 'news' in statement:

            news = webbrowser.open_new_tab("https://rudaw.com/home")

            speak('Here are some headlines from the Times of Erbil,Happy reading')

            time.sleep(6)



 



        elif 'search'  in statement:

            statement = statement.replace("search", "")

            webbrowser.open_new_tab(statement)

            time.sleep(5)



        elif 'ask' in statement:

            speak('what question do you want to ask now')

            question=takeCommand()

            app_id="R2K75H-7ELALHR35X"

            client = wolframalpha.Client('R2K75H-7ELALHR35X')

            res = client.query(question)

            answer = next(res.results).text

            speak(answer)

            print(answer)





        elif "log off" in statement or "sign out" in statement:

            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")

            subprocess.call(["shutdown", "/l"])



time.sleep(3)

















