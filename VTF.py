import pyttsx3
friend = pyttsx3.init()
speech = input ("Say So,Something: ")
friend.say("Hello , Good morning")
friend.say(speech)
friend.runAndWait()