# Rule-based AI chatbot using Python

import datetime
import time

name=input("Hi enter your name:")
presentHour=datetime.datetime.now().hour

if 5<=presentHour<=11:
    print("Good morning ,",name)
elif 12<=presentHour<=17:
    print("Good afternoon,",name)
elif 17<=presentHour<=20:
    print("Good Evening,",name)
else:
    print("Good night,",name)



print("Welcome to AI based chatbot")
print("Please ask your question , type bye to exit")

# memory creation of boat
responses={
    "hello":"hi how can i help you?",
    "how are you":"I am fine, Thank you",
    "who are you":"I am smart AI chatbot created by Shailesh ",
    "motivate me":"Keep goning Your project bug that you find that you make great dvolper",
    "happy":"I glad to see you",
    "function kya hota hai":"ja kar chapter 7 padho"
}

# method to get response from chatbot

def getResOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I aam not able to tell..."

# take user input
 
while True:
    userInput=input("Ask your question ? ")
    reply=getResOfBot(userInput)
    time.sleep(2)
    print("Bot Message:",reply)

    if "bye" in userInput.lower():
        print("Goodbye have a nice day")
        break
