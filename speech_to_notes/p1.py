import speech_recognition as sr

r= sr.Recognizer()

def wfile():
    harvard = sr.AudioFile('a.wav')
    with harvard as source:
        audio=r.record(source)	
    t=r.recognize_google(audio)
    f= open("cdoc.txt","w")
    f.write(t)
    return

wfile()
