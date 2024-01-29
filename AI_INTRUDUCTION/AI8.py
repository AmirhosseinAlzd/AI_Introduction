import speech_recognition as sr 
import pyttsx3

r = sr.Recognizer()

dataframe = {
	"hello":['hello' , "hey" , "welcome to app"] ,
	"hey":['hello' , "hey" , "welcome to app"] ,
	"hi": ['hello' , "hey" , "welcome to app"] ,
	"pc" : ['hello' , "hey" , "welcome to app"] 
	,"bye":['bye' , 'have a nice day' , "goodbye"],
	"goodbye":['bye' , 'have a nice day' , "goodbye"],
}

name = "pc"

def check(inp):
    data = inp.split(" ")
    for i in data:
        for j in dataframe.keys():
            if i == j:
                return j

def textprocess(inp):
    import random
    if inp in dataframe.keys():
        data = dataframe[inp]
        x = random.choice(data)
        return x

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
    

while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ",MyText)
            if name in MyText.split(" "):
                MyText2 =check(MyText)
                data = textprocess(MyText2)
                SpeakText(data)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
