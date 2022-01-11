# text_reader.py
""" This Python program uses text to speech conversion for interacting with a user. """

import pyttsx3 as sx

def initialize_engine():
    speech_engine = sx.init()
    speech_engine.say("Hello! My name is speech reader 001, a simple text to speech program.")
    speech_engine.say("What is your name dear user? ")
    speech_engine.runAndWait()
    return speech_engine

def get_user_name():
    user_name = input("Enter name here: ")
    return user_name.strip(" ")


def greet_user(speech_engine, user_name):
    speech_engine.say(f"Pleased to meet you {user_name}. How are you doing today?")
    speech_engine.runAndWait()
    return True


def main():
    speech_engine = initialize_engine()
    user_name = get_user_name()
    greet_user(speech_engine, user_name)


if __name__ == '__main__':
    main()
