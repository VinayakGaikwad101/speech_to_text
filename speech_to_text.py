import os
import vosk
import sounddevice as sd
import json
import numpy as np
import keyboard


def main():
    print("Choose a model:")
    print("1: Indian English (vosk-model-small-en-in-0.4)")
    print("2: American English (vosk-model-small-en-us-0.15)")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        model_path = "models/vosk-model-small-en-in-0.4"
    elif choice == "2":
        model_path = "models/vosk-model-small-en-us-0.15"
    else:
        print("Invalid choice. Exiting...")
        return

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)

    def callback(indata, frames, time, status):
        audio_data = np.frombuffer(indata, dtype=np.int16)
        if recognizer.AcceptWaveform(audio_data.tobytes()):
            result = recognizer.Result()
            result_dict = json.loads(result)
            text = result_dict.get("text", "")
            text_with_fullstop = text + ". "  # Add full stop after each recognized segment
            print(f"Recognized Text: {text_with_fullstop}")
            with open("output.txt", "a") as file:
                file.write(text_with_fullstop + "\n")

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening... Press Ctrl + Q to stop.")

        # Keep the script running until Ctrl + Q is pressed
        try:
            while True:
                if keyboard.is_pressed('ctrl+q'):
                    print("Ctrl + Q pressed. Stopping...")
                    break
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
