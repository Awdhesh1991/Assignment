import json

with open('awdhesh.json', 'r') as file:
    awdhesh_data = file.read()

av= json.loads(awdhesh_data)

def taking_input():
    Account_Number=int(input("Enter your account number : "))
    if Account_Number==av["Account_number"]:
        ATM_pin=int(input("Enter your atm pin : "))
        if ATM_pin==av["ATM_pin"]:
            Account_Type=input("Enter your account type : ")
            if Account_Type==av["Account"]:
                Mobile_Number=int(input("Enter your Mobile Number : "))
                if Mobile_Number==av["Mobile_number"]:
                    print(av["Balance"])
                    Amount=int(input("Enter the ammount you want to withdrawl"))    
                    if  av["Balance"]>0:
                        if (av["Balance"] - Amount)>0:
                            print(f"You have Credited by {Amount} and your updated Balance is {av['Balance']-Amount}")
                        else:
                            print("There is insufficient amount in Your Account")
                    else:               
                        print("There is insufficient amount in Your Account")
                else:
                    print("You have Enter wrong mobile number ")
            else:
                print("You have Enter wrong Account type ")
        else:
            print("You have Enter wrong Atm Pin ")
    else:
        print("You have Enter wrong Account number ")
    

taking_input()
