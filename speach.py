import speech_recognition as sr


def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говори")
        audio = r.listen(source)

    return r.recognize_google(audio, language='ru-RU')
print(audio())