import pyttsx3
import speech_recognition
from datetime import date, datetime
import sys
open=1
close=2
message= int(input('input message:'))
if message==1:
    def voice_recognition():
        robot_ear=speech_recognition.Recognizer()
        robot_mouth= pyttsx3.init()
        robot_brain=""
        while True:
            with speech_recognition.Microphone() as mic:
                print("Robot: Password Authentication Please")
                audio=robot_ear.listen(mic)

            print("Robot:...")

            try:
                you=robot_ear.recognize_google(audio)
            except:
                you=""

            print("You: " + you)


            if you=="":
                robot_brain="I can't hear you, try again"
            elif 'hello' in you:
                robot_brain="Congratulation, correct password"
                return True
            elif "stop" in you:
                robot_brain='Goodbye'
                print("Robot:"+ robot_brain)
                robot_mouth.say(robot_brain)
                robot_mouth.runAndWait()
                sys.exit()
            else:
                robot_brain="Wrong password, try again"
                return False

            print("Robot:"+ robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
    voice_recognition()
elif message == 2 :
    print("system will be close right now.")
    sys.exit()
else :
    print("Wrong")
    return False
    sys.exit()
