import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)  # Uncomment to see available voices
engine.setProperty('voice', voices[0].id)  


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!") 
    speak("i am jarvis please tell me how may i help you")

def takecommand():
    """
    It takes microphone input from the user and returns it as a string.
    If the speech is not recognized, it returns 'None'.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Sorry, I did not understand that. Please say it again.")
        return "None"
    return query

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUREMAIL@gmail.com', 'your_password_here')
    server.sendmail(to, content)
    server.close()

if __name__ == "__main__":
    wish_me()
    #while True:
    if 1:
        query = takecommand().lower()
        
        #logic to handle the query can be added here
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  
        elif 'open google' in query:
            webbrowser.open("google.com")    
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = "D:\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
            # You can add code to play music from a specific source or library
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\varsh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'email to varsh' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "varshney.dev.013.com"#your email address
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")
            
        else:
            speak("I am not sure how to help with that.")

    # Add more functionality here as needed
    # For example, you can implement a command listener or other features