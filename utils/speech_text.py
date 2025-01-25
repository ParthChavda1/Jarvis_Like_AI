import speech_recognition as sr
import pyttsx3
import keyboard
import sys


class SpeechTextHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300
        self.speaker_engine = pyttsx3.init()

    # Function to listen to the microphone with key binding
    def listen_untill_release(self) -> str:
        audio_data = bytearray()  # Store raw audio data here

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening....!")
            while keyboard.is_pressed("space"):
                sys.stdin.flush()
                try:
                    audio = self.recognizer.record(source, duration=1)
                    audio_data.extend(
                        audio.get_raw_data()
                    )  # Add raw audio data to the bytearray
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Error: {e}")
            # print("Got out of the listening Phase, Now converting")
        # Create an AudioData object from the concatenated raw audio data
        combined_audio = sr.AudioData(
            bytes(audio_data), source.SAMPLE_RATE, source.SAMPLE_WIDTH
        )

        # Perform recognition on the combined audio
        try:
            text = self.recognizer.recognize_google(combined_audio)
            # print("Recognition complete.")
        except sr.UnknownValueError:
            text = None
        except sr.RequestError as e:
            text = None

        return text

    # text to audio ==>
    def speak_text(self, text) -> None:
        self.speaker_engine.say(text)
        self.speaker_engine.runAndWait()

    def __del__(self):
        self.speaker_engine.stop()
