import pyttsx3

engine = pyttsx3.init()

text = input("Enter text to be spoken: ")

engine.say(text)
engine.runAndWait()
