from utils.speech_text import SpeechTextHandler
from utils.model import ReplyModel

import keyboard
import sys

# Main loop
if __name__ == "__main__":
    speech_text_handler = SpeechTextHandler()
    model = ReplyModel()
    print("Press and hold 'Space' to start, release to stop. Say 'exit' to exit.")
    while True:
        if keyboard.is_pressed("space"):
            # flush the buffer
            sys.stdin.flush()

            # listen to the audio
            listened_text = speech_text_handler.listen_untill_release()

            # Bad text handling
            if not listened_text:
                print("Please speak again")
                continue

            # print the text
            print(f"text: {listened_text}")
            if not (listened_text.find("exit") == -1):
                break
            print("Generating response...")
            result = model.reply(listened_text)
            print(f"text: {result}")

            speech_text_handler.speak_text(result)
    print("Exiting...")
