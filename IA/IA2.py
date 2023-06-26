import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Inicialização do reconhecimento de fala
r = sr.Recognizer()

# Inicialização da síntese de fala
engine = pyttsx3.init()

# Função para falar a resposta
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para ouvir o comando de voz
def listen():
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Desculpe, não entendi.")
        except sr.RequestError as e:
            print(f"Erro ao fazer a solicitação ao serviço de reconhecimento de fala: {e}")
    return ""

# Função para processar o comando
def process_command(command):
    if "olá" in command:
        speak("Olá, como posso ajudar?")
    elif "horas" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"Agora são {current_time}")
    elif "pesquisar" in command:
        query = command.replace("pesquisar", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("Aqui está o que encontrei:")
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Houve um problema ao pesquisar. Por favor, seja mais específico.")
    elif "sair" in command:
        speak("Até logo!")
        exit()
    else:
        speak("Desculpe, não entendi o comando.")

# Loop principal do assistente
while True:
    command = listen()
    process_command(command)
