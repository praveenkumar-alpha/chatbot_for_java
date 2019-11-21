from chatterbot import ChatBot
'''
import pyttsx3
from gtts import gTTS
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('chatbot : ' + audio)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        speak('Your last command couldn\'t be heard.')
        command = myCommand();

    return command

'''
chatbot=ChatBot(
    'Ron Obvious',
    trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.train("chatterbot.corpus.english")
while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print(response)
