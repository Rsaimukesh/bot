import pyttsx3


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

eng=str("english")
tam=str("tamil")
print(eng)
print(tam)
print("select language")
lang=input("tamil or english")
if lang==eng:
    
        def health_chatbot():
            speak("Select language")
            speak("Hi, I'm an AI doctor. What can I do for you?")
            speak("Enter your name:  ")
            name = input("Enter your name:  ")
            speak("How are you, " + name + "?")
            speak(name + ", enter your age.  ")
            age = input(name + ", enter your age: ")

            while True:
                user_input = input("You:  ")
                
                if "hello" in user_input or "hi" in user_input:
                    speak("Hello! How can I help you with your health today?")
                    
                elif "quit" in user_input or "exit" in user_input:
                    speak("Goodbye! Take care of your health.")
                    break

                elif "i am suffering from fever" in user_input:
                    # handle fever
                    pass

                elif "check fever" in user_input:
                    temp = float(input("Enter your temperature: "))
                    sym = input("Enter any symptoms (comma-separated): ").split(',')
                    
                    if temp > 99.5 or any(sym in sym for sym in ['headache', 'body pain']):
                        speak("You may have a fever.")
                        print("You may have a fever.")
                        print("If you want a tablet, type 'tablet for fever'.")
                        speak("If you want a tablet, type 'tablet for fever'.")
                    else:
                        speak("You may not have a fever.")
                        print("You may not have a fever.")
                
                elif "tablet for cough" in user_input:
                    speak("Dextromethorphan is a common ingredient in many OTC cough medicines.")

                 
                elif "help" in user_input:
                    speak(" i can able to give you medical information like booking appoinment,online consultation,medical assit and  tablet for fever,cough,headache etc")
                
                elif "tablet for headache" in user_input:
                    speak("Aspirin is an NSAID that is often used to treat headaches. It can be effective in reducing pain.")

                elif "appoinment" in user_input:
                    speak("enter name ")
                    name=input("enter name :")
                    speak("enter Age ")
                    age=int(input("enter age :"))
                    speak("enter time ")
                    time=int(input("Enter date and time"))
                    print("booked")

                
                elif "tablet for body pain" in user_input:
                    speak("Codeine is used for moderate to severe pain relief and can also reduce cough.")
                
                else:
                    speak("I cannot understand you.")
                    print("I cannot understand you.")

        health_chatbot()
elif lang==tam:
    print("the is not programed")