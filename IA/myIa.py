import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="pt-BR")
            command = command.lower()
            if "jarvis" in command:
                command = command.replace("jarvis", "")
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = listen()
    if "tocar" in command:
        song = command.replace("tocar", "")
        speak("Tocando " + song)
        pywhatkit.playonyt(song)
    elif "tempo" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Agora são " + time)
    elif "pesquisar" in command:
        search = command.replace("pesquisar", "")
        info = wikipedia.summary(search, 1)
        speak(info)
    else:
        speak("Desculpe, não entendi o comando.")

while True:
    run_jarvis()
