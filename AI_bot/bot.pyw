#Importing neccessary modules
import subprocess
try:
    import os
    import datetime
    import wikipedia
    import webbrowser
    import speech_recognition as sr 
    import pyttsx3 as ts
    import sys
    import pyjokes
except:
    subprocess.call
ran = 0
engine = ts.init('sapi5')

#Initializing voice for Bot
voices = engine.getProperty('voices')
#print(voices[0])
engine.setProperty('voice',voices[1].id)

class Mybot: 
    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()
        
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        print(hour)
        if(hour < 12 ):
            self.speak("Hi Sir, Good Morning")
        elif(hour >= 12 and hour < 16):
            self.speak("Hi Sir, Good Afternoon")
        elif(hour >= 16 and hour < 19 ):
            self.speak("Hi Sir, Good Evening")
        else:
            self.speak("Hi Sir, Good Night")
    
    def takeCommand(self):
        #It takes microphone input from the user and returns string output
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                print("Recognizing...")
                command = recognizer.recognize_google(audio)
                print(command)
                return command
        except Exception as e:
            print(str(e))
            self.speak("Sorry Madam. Can you say that again please?")
            return None
                    
if __name__ == '__main__':
    while True:
        try:
            bot = Mybot()
            if(ran == 0):
                greet = "I am CA ,What can I do for you?"
                bot.wishMe()
                bot.speak(greet)
                ran = 1
                
            cmd = bot.takeCommand()   
            if(cmd != None):
                cmd = cmd.lower()
                if 'wikipedia' in cmd:
                    cmd = cmd.replace('wikipedia','')
                    print(cmd)
                    results = wikipedia.summary(cmd,sentences=2)
                    bot.speak("Accordind to wiki ")
                    bot.speak(results)
                elif 'time' in cmd:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    bot.speak("Current time is "+time)    
                elif('open youtube'in cmd) or ('youtube' in cmd):
                    webbrowser.open('www.youtube.com')       
                elif('joke' in cmd):
                    bot.speak(pyjokes.get_joke())
                elif ('play music'  in cmd) or ('play song'in cmd) or ('play'in cmd):
                    webbrowser.open('https://music.youtube.com/watch?v=4z-oDk1utVo&list=PLr0GeYsyVUYloJFMVrHEJ7FzMcWuN7Q7C')        
                elif ('exit' or 'stop') in cmd:
                    Mybot().speak("Exiting the program . I will be back Akanksha Madam") 
                    exit(0)    
        except Exception as e: 
            Mybot().speak(str(e)) 
            Mybot().speak("Exiting the program . I will be back Madam") 
            sys.exit()      
            
     





