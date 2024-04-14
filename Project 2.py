from win32com.client import Dispatch
import json

speak = Dispatch("SAPI.SpVoice")
speak.Voice = speak.GetVoices().Item(1)

with open('awdhesh.json', 'r') as file:
    awdhesh_data = file.read()

av= json.loads(awdhesh_data)

def taking_input():
    speak.Speak("Enter your account number : ")
    Account_Number=int(input("Enter your account number : "))
    if Account_Number==av["Account_number"]:
        speak.Speak("Enter your atm pin : ")
        ATM_pin=int(input("Enter your atm pin : "))
        if ATM_pin==av["ATM_pin"]:
            speak.Speak("Enter your account type : ")
            Account_Type=input("Enter your account type : ")
            if Account_Type==av["Account"]:
                speak.Speak("Enter your mobile number : ")
                Mobile_Number=int(input("Enter your Mobile Number : "))
                if Mobile_Number==av["Mobile_number"]:
                    print(av["Balance"])
                    speak.Speak("Enter the ammount you want to withdrawl")
                    Amount=int(input("Enter the ammount you want to withdrawl"))    
                    if  av["Balance"]>0:
                        if (av["Balance"] - Amount)>0:
                            speak.Speak(f"You have Credited by {Amount} and your updated Balance is {av['Balance']-Amount}")
                            print(f"You have Credited by {Amount} and your updated Balance is {av['Balance']-Amount}")
                        else:
                            speak.Speak("There is insufficient amount in Your Account")
                            print("There is insufficient amount in Your Account")
                    else:               
                        speak.Speak("There is insufficient amount in Your Account")
                        print("There is insufficient amount in Your Account")
                else:
                    speak.Speak("You have Enter wrong mobile number ")
                    print("You have Enter wrong mobile number ")
            else:
                speak.Speak("You have Enter wrong Account type ")
                print("You have Enter wrong Account type ")
        else:
            speak.Speak("You have Enter wrong Atm Pin ")
            print("You have Enter wrong Atm Pin ")
    else:
        speak.Speak("You have Enter wrong Account number ")
        print("You have Enter wrong Account number ")
    

taking_input()
