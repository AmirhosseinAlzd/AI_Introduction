
import pyttsx3 

l = {
          "hello":['hey' , 'hi' , 'pc' , 'hello'] , 
          "bye":['goodbye' , 'bye' , 'see you later' , 'see you soon']
      }
def check(inp):
    data = inp.split(" ")
    for i in data:
        for j in l['hello']:
            if i == j:
                return j

engine = pyttsx3.init()  
text = input("Enter your text: ")  
data = check(text)
engine.say(data)
engine.runAndWait() 

