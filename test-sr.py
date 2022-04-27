import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

filename = "audio-test-2.wav"

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_sphinx(audio_data)
    print(text)
