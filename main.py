import speech_recognition as sr
import pyttsx3
import datetime

# Text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Audio Input Function:
def get_audio():
    with sr.Microphone() as source:
        # Speech recognition setup
        recognizer = sr.Recognizer()
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Assistant Function:

def assistant(command):
    if "hello" in command:
        print("V_A: Hello! How can I help you today?")
        speak("Hello! How can I help you today?")
        print(" I can assist on current time and date ")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"V_A: The current time is {current_time}")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"V_A: Today's date is {current_date}")
        speak(f"Today's date is {current_date}")

    elif "quit" in command:
        print("V_A: Goodbye!")
        speak("Goodbye!")
        exit()

# Main Execution:
if __name__ == "__main__":
    print("V_A: Hello! I am your voice assistant. How can I help you today?")
    speak("Hello! I am your voice assistant. How can I help you today?")

    while True:
        user_command = get_audio()
        if user_command:
            assistant(user_command)
