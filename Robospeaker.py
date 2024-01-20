import win32com.client

if __name__ == "__main__":
    print("Welcome to Robo speaker 1.1 created by Manav Alag")

    # Created a SpVoice object
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    while True:
        text_to_speak = input("Enter what you want to speak:")

        if text_to_speak.lower() == "q":
            a="good bye!"
            speaker.Speak(a)
            print(a)
            break

        # Using the SpVoice object to speak the entered text
        speaker.Speak(text_to_speak)

    