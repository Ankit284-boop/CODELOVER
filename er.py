import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    speak("I am Jarvis Sir. Please tell me how may I help you")
    while True:
        query = takeCommand().lower()
        if 'open google' in query:
            os.startfile(
                "C:\Program Files\Google\Chrome\Application\Chrome.exe")
            speak("Opened Google Sir, please tell me what to do now.")
            pyautogui.hotkey('win', 'up')

            while True:
                i = True
                bubu = takeCommand().lower()
                if 'maximize' in bubu:
                    if i == False:
                        pyautogui.hotkey('win', 'up')
                        i = True
                    else:
                        speak("SIR,YOUR CHROME IS ALREADY MAXIMISED")

                    speak("SIR,YOUR CHROME IS ALREADY  MAXIMIZED")
                if 'minimise' in bubu:
                    if i == True:
                        pyautogui.hotkey('win', 'down')
                        i = False
                        speak("SIR,YOUR CHROME HAS BEEN MIMIMISED")
                    else:
                        speak("SIR,YOUR CHROME IS  ALREADY MINIMISED")

                if 'open youtube' in bubu:
                    with sr.Microphone() as source:
                        speak("SIR PLEASE TELL WHAT DO YOU SEARCH IN YOUTUBE?")
                        query1 = takeCommand()
                        webbrowser.open(
                            "https://www.youtube.com/search?q=" + query1)
                        speak("SIR,SEARCHED YOUR QUERY"+query1)
                if 'google' in bubu:
                    with sr.Microphone() as source:
                        speak("PLEASE TELL TO SEARCH GOOGLE")
                        query2 = takeCommand()
                        webbrowser.open_new_tab(
                            "https://www.google.com/search?q=" + query2)

                elif 'jarvis quit' in bubu:
                    break
