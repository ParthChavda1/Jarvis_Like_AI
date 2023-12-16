import speech_recognition as sr
import pyttsx3
import keyboard

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen to the microphone
def record_text():
    with sr.Microphone() as source:
        print("Listening...")
        print('Press Enter to stop Listening')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        keyboard.wait('Enter')
        
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error: {e}"
    
#function to speak what it listens
def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Main loop
while True:
    input("Press Enter to start speaking ")
    spoken_text = record_text()
    print(spoken_text)
    speak_text(spoken_text)
