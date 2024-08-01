import speech_recognition as sr
import pyttsx3
import keyboard
import sys
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
    Answer the question below

    Here is conversation history : {context}

    Question = {question}


    Answer:
"""

model = OllamaLLM(model="llama3:8b")
prompt = ChatPromptTemplate.from_template(template= template)
chain = prompt | model



# Initialize the recognizer
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

cxt = ""
# generate reply from llm model
def generate_text(listened_text):
    global cxt
    input_data = {
        "context": cxt,
        "question": listened_text
    }
    result = chain.invoke(input = input_data)
    cxt += f"/nUser: {listened_text}/n AI:{result}"
    return result


# text to audio ==>
def speak_text(text) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Function to listen to the microphone with key binding
def listen_untill_release() -> str:
    audio_data = bytearray()  # Store raw audio data here

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening....!")
        while keyboard.is_pressed("space"):
            sys.stdin.flush()
            try:
                audio = recognizer.record(source, duration=1)
                audio_data.extend(
                    audio.get_raw_data()
                )  # Add raw audio data to the bytearray
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error: {e}")
        print("Got out of the listening Phase, Now converting")
    # Create an AudioData object from the concatenated raw audio data
    combined_audio = sr.AudioData(
        bytes(audio_data), source.SAMPLE_RATE, source.SAMPLE_WIDTH
    )

    # Perform recognition on the combined audio
    try:
        text = recognizer.recognize_google(combined_audio)
        print("Recognition complete.")
    except sr.UnknownValueError:
        text = None
    except sr.RequestError as e:
        text = None

    return text


# Main loop
if __name__ == "__main__":
    print("Press and hold 'Space' to start, release to stop.")
    while True:
        if keyboard.is_pressed("space"):
            # flush the buffer
            sys.stdin.flush()

            # listen to the audio
            listened_text = listen_untill_release()

            # Bad text handling
            if not listened_text:
                print("Please speak again")
                continue

            # print the text
            print(f"text: {listened_text}")
            if not (listened_text.find("exit") == -1):
                break
            print("Generating response...")
            result = generate_text(listened_text)
            print(f"text: {result}")

            speak_text(result)

            

            print("Done!")
