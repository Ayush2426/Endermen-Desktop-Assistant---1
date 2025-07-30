import speech_recognition as sr
import webbrowser
import os
from openai import OpenAI
import pyttsx3
import random
import openai
import datetime
opencode = False
res = False
mongodb = False

def ai(prompt):
    client = OpenAI(
        api_key="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"
    )
    text = f"Endermen's response for the user's query: {prompt}\n\n*********_________*********__________*********__________\n"

    response = client.responses.create(
    model="gpt-4o-mini",
    temperature=0.7,
    input=prompt,
    store=True,
    )
    
    try:
        print(response.output_text)
        text += response.output_text
    except Exception as e:
        return "No user input found!!"
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
    
    with open(f"OpenAI/Prompt - {prompt[0,15]}", "w") as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def userCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return("An error occurred!")

if __name__ == "__main__":
    print('Endermen')
    say("Hello Im Shogun A.I. here!")
    while True:
        print("Listening...")
        query = userCommand().lower()
        sites = [["Youtube" , "https://youtube.com"], ["Wikipedia", "https://wikipedia.com"], ["Amazon", "https://amazon.com"], ["Netflix", "https://netflix.in"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])
            if f"exit".lower() in query.lower():
                say("Pleasure assisting you sir!!")
                exit()
            if f"time data" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")
            if f"Open vs code".lower() in query.lower() and not opencode:
                vs = r"C:\Users\av874\AppData\Local\Programs\Microsoft VS Code\code.exe"
                os.startfile(vs)
                opencode = True
            if f"Open mongodb".lower() in query.lower() and not mongodb:
                md = r"C:\Users\av874\AppData\Local\MongoDBCompass\MongoDBCompass.exe"
                os.startfile(md)
                mongodb = True
            if f"Using Artificial Intelligence".lower() in query.lower() and not res:
                ai(prompt=query)
                res = True
            if f"Endermen".lower in query.lower() and not res:
                ai(prompt=query)

            # say(text)