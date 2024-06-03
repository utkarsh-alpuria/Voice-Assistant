# import modules
import time 
import threading # to creat threads
import speech_recognition as sr # for recognizing audio
import subprocess # to call command.bat file
import eel

class wake_word_listener(threading.Thread): # defining the "wake_word_listener" class with "Thread" as its parent class
    def __init__(self):
        super(wake_word_listener, self).__init__() # initializing "Thread" part of "wake_word_listener" class so that when a object is created it will execute "run" method of "Thread"
        self.must_listen = False
        pass
    
    def start_stop(self, must_listen): # called when start_stop_button is clicked
        self.must_listen = not self.must_listen # toggle start and stop
        print(f"must_listen = {self.must_listen}")
        # if self.must_listen:

    @eel.expose
    def run(self): # will start executing as soon as the "wake_word_listener" object is created
        while True:
            # print("run")
            if self.must_listen: # if start is clicked
                recognizer = sr.Recognizer()
                with sr.Microphone() as audio_source:
                    print("Listening...")
                    eel.showListening()
                    audio = recognizer.listen(audio_source)
                    try:
                        # audio_to_text = recognizer.recognize_google(audio)
                        audio_to_text = recognizer.recognize_whisper(audio, language="english", translate=True)
                        if audio_to_text.strip().replace(".", "").replace("!", "").lower() == "hey jarvis" :
                            print("JARVIS ACTIVATED!")
                            eel.jarvisActivated()
                            
                    except sr.UnknownValueError:
                        print("Sorry, could not understand audio")
                        # return None
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                        # return None  
            else:
                time.sleep(1)
            
            
        




        
    

