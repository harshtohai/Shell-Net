from data import allvar
from Main_Body_Functions.update_upload import updating_user
from os import system
from error_handeling import error_handel


@error_handel
def updateprofile(userinfo):
    updateprofileinput = input(f"{userinfo.get('Name')} What would you like to update? 'Name', 'Username', 'Emailid', 'Password', 'DOB', 'Gender', 'Bio', 'Field' or type 'Exit'.")
    
    if updateprofileinput in allvar: 
        if updateprofileinput == "Password":
            askingforpass = input("Enter your Password to create new Password\n: ")
            if askingforpass == userinfo.get('Password'):
                newpass = input("Now enter a New Password.\n: ")
                userinfo.update({'Password' : newpass})
                print("Your New Password is being set as "+userinfo['Password'])
                updating_user(updateprofileinput, newpass,userinfo)
            else: 
                print('Incorrect Password try again.')
        else: 
            updatingfield = input(f"What do you want your new {updateprofileinput} to be: ")
            userinfo.update({updateprofileinput:updatingfield})
            updating_user(updateprofileinput, updatingfield,userinfo)
        while True: 
            askingmore = input("Wanna update more? 'Y' or 'N'")
            if askingmore == 'Y':
                updateprofile()
                
            elif askingmore == 'N':
                print("Ok your profile is update use command 'ViewProfile' to see updates")
                system('cls')
                break
            elif askingmore == 'Exit':
                print("Press Ctrl + C to exit")
            else:
                print("Not a right command. Try Again...")
    elif updateprofileinput == 'Back':
        print("Directed to Menu...")
        system('cls')
        pass
    elif updateprofileinput == 'Exit':
        exit()        
    else:
        print("Not what we exptected. Try Again with correct command.")   
        updateprofile()      