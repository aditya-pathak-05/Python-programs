import pyttsx3
a=pyttsx3.init()
b=input("ENTER THE TEXT THAT YOU WANT TO SPEAK")
a.say(b)
a.runAndWait()