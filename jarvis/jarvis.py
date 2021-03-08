from collections import ChainMap
import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" 
    # Use female voice 
    engine.setProperty('voice', voice_id)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("jarvis at your service, Please tell me how can i help you?")

def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("example.gmail.com", "password")
    server.sendmail("example.gmail.com", to, content)
    server.close

def scteenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\User\\Desktop\\jarvis\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def voice():
    voices = engine.getProperty('voices') 

    for voice in voices: 
        # to get the info. about various voices in our PC  
        print("Voice:") 
        print("ID: %s" %voice.id) 
        print("Name: %s" %voice.name) 
        print("Age: %s" %voice.age) 
        print("Gender: %s" %voice.gender) 
        print("Languages Known: %s" %voice.languages) 

def brave():
    speak("what should i search?")
    wb.register('brave',
                None,
	        wb.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
    search = takeComand().lower()
    base_url = "http://www.google.com/?#q="
    final_url = base_url + search.replace(" ","%20")
    wb.get("brave").open_new_tab(final_url)

if __name__ == "__main__":
    wishme()
    while True:
        query = takeComand().lower()

        if "time" in query:
            time()
        
        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeComand()
                to = "xyz@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")

            except Exception as e:
                print(e)
                speak("Unable to send the email!")

        elif "search in chrome" in query:
            speak("what should i search?")
            wb.register('chrome',
                None,
	        wb.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            search = takeComand().lower()
            wb.get("chrome").open_new_tab(search +".com")

        elif "logout" in query:
            os.system("shutdown -l")
            
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir = "D:\\mp3"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("What should I remember?")
            data = takeComand()
            speak("you said me to remember that "+ data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that "+ remember.read())

        elif "screenshot" in query:
            scteenshot()
            speak("Done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "voice" in query:
            voice()

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

        elif "search" in query:
            brave()

        elif "offline" in query:
            speak("thank you, see you again!")
            quit()