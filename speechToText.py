import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen to the microphone
def record_text():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error: {e}"

# Main loop
while True:
    input("Press Enter to start speaking ")
    spoken_text = record_text()
    print(spoken_text)
