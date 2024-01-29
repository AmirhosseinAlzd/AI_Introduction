
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def sayethetime():
    import datetime
    data = datetime.datetime.now()
    return data


def isiteafunction(inp):
    if type(inp) == type(isiteafunction):
        return True
    return False


l = ['hello' , 'hey' , 'hi' , 'pc' , 'bay' , 'goodbye' , "time" , "forward" , "left" , "right" , "backward"]

dataframe = {
	"hello":['hello' , "hey" , "welcom to app"] ,
	"hey":['hello' , "hey" , "welcom to app"] ,
	"hi": ['hello' , "hey" , "welcom to app"] ,
	"pc" : ['hello' , "hey" , "welcom to app"] 
	,"bay":['bay' , 'have a nice day' , "goodbay"],
	"goodbye":['bay' , 'have a nice day' , "goodbay"]
	, "time" : sayethetime
}


name = "test"

def listen():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ",MyText)
            return MyText
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)
    except sr.UnknownValueError:
        return "unknown error occurred" 


def learn(inp):
    l.append(inp)
    SpeakText(f"idont know {inp} what dose mean can you tell me what shoud i say in ancer ??")
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ",MyText)
            try:
                MyText = MyText.replace("say" , "")
            except:
                pass
            dataframe.update({inp : [MyText]})
            print(dataframe)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred") 
	


def textprocess(inp):
	import random
	found = False
	for i in l:
		if i in inp:
			found = True
			break
	if found : 
		data = dataframe[i]
		if isiteafunction(data):
			return data()
		else:
			x = random.choice(data)
			return x
	else:
		learn(inp)
		


def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()




import cv2 


camera = cv2.VideoCapture(0) 

face_cascade = cv2.CascadeClassifier('face.xml') 
eye_cascade = cv2.CascadeClassifier('eye.xml') 


while True:
	seen = False
	cam , fream = camera.read() 
	gray_frame=cv2.cvtColor(fream,cv2.COLOR_BGR2GRAY) 
	face=face_cascade.detectMultiScale(gray_frame,1.3,5)
	for (x,y,w,h) in face:
		cv2.rectangle(fream,(x,y),(x+w,y+h),(0,0,255),thickness=4) 
		gray_face=gray_frame[y:y+h,x:x+w] 
		color_face=fream[y:y+h,x:x+w] 
		eye=eye_cascade.detectMultiScale(gray_face,1.3,5) 
		for (a,b,c,d) in eye:
			cv2.rectangle(color_face,(a,b),(a+c,b+d),(0,255,0),thickness=4) 
			seen = True
			
	if cv2.waitKey(1) & 0xff == ord("e"): 
		break
	output = listen()
	if name in output or seen:
		data = textprocess(output.replace(f" {name}" , ""))
		SpeakText(data)
