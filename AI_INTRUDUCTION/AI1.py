import pyttsx3 
def changevoice(): 
    engine = pyttsx3.init() 
    voice=engine.getProperty('voices')
    v=input("Do you want to hear lady voice or man voice?")
    '''while True:'''
    if v=='lady voice':
        v=1
    elif v=='man voice':
        v=0
    engine.setProperty('voice',voice[v].id)
    text = input("Enter your text: ")
    engine.say(text)  
    engine.runAndWait() 
changevoice()
