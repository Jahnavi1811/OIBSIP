import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text to speech engine
engine = pyttsx3.init()

def greet():
    engine.say("Hello! How can I assist you today?")
    engine.runAndWait()

def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the Google API.")
        return ""

def respond(command):
    if "hello" in command:
        engine.say("Hello there!")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        engine.say(f"The current time is {now}.")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        engine.say(f"Today is {today}.")
    elif "search" in command:
        engine.say("What would you like me to search for?")
        engine.runAndWait()
        search_term = get_command()
        if search_term:
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open(url)
    else:
        engine.say("I'm sorry, I didn't understand that command.")

    engine.runAndWait()

if __name__ == "__main__":
    greet()
    while True:
        command = get_command()
        if command == "exit":
            break
        respond(command)
