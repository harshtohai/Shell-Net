import datetime
from Main_three.main_body import maincontent
from data import userpersona,userinfo,remainders,registerlist
from Main_Body_Functions.update_upload import uploading_data,updating_user
from Dual_Usage_Functions.clrscr import clrscr
from error_handeling import error_handel


@error_handel
def register():
    for i in registerlist: 
        if i == 'Username':                    
            def usernamehandle():
                registerinput = input(f"Enter your {i} : ")
                
                if userpersona.find_one({'Username': registerinput.lower()}) == None or registerinput != '':                       
                    userinfo.update({'Username': registerinput})
                else :
                        print('Username is already taken.. Try with something new')
                        usernamehandle()

            usernamehandle()
        elif i == 'Password':
            def countingpass():
                registerinput = input(f"Enter your {i} : ")
                
                if len(registerinput)> 7:
                    userinfo.update({'Password':registerinput})
                else:
                        print('Password must be greater than 8 characters.')
                        countingpass()
            countingpass()
        elif i == 'Emailid':
            def validateEmail():
                registerinput = input(f"Enter your {i} : ")
                
                if registerinput.find('@') == -1 :
                    print('Invalid Email')
                    validateEmail()
                elif registerinput[-4:] != '.com' or registerinput[-4] == '@' :
                    print('Invalid Email')
                    validateEmail()
                else:
                    userinfo.update({'Emailid':registerinput})
            validateEmail()
        elif i == 'DOB':
            def checkingDOB():
                
                registerinput = input(f"Enter your DOB Date of Birth eg 2022/12/01: ")
                try:
                    datetime.datetime.strptime(registerinput,'%Y/%m/%d')
                    userinfo.update({'DOB':registerinput})
                    
                except Exception as e:
                    if type(e) == ValueError:
                        
                        print('Invalid Date or Format')  
                        checkingDOB()
                                        
            checkingDOB()
        else:
            def othervalues(i):
                registerinput = input(f"Enter your {i} : ")
                if registerinput != '':
                    userinfo.update({i:registerinput})
                else:
                    print('Must enter an value')
                    othervalues(i)
            othervalues(i)   

    uploading_data(userinfo)    
    print(f"Hello {userinfo.get('Name')} This is your user persona")
    for i in registerlist:
        print(f"Your {i} is : {userinfo.get(i)}") 
        
    userinfo['Posts'].append(f"Hello There!! I am {userinfo['Name']} and I am Looking forward to connect with you..")
    gettingdate  = datetime.datetime.now()
    userinfo['Time'].append(f"{gettingdate.month}/{gettingdate.day}")
    userinfo['Likes'].append(0)
      
    while True: 
        moredetails = input(f"Do you want to set details sucha as 'Bio' and 'Field' Y or N ?")
        if moredetails == "Y":
            print("Ok ")    
            for i in remainders: 
                forupdating=input(f"Enter your {i}: ")
                userinfo.update({i: forupdating})
                updating_user(i, forupdating)
            print("Great.. Your Account setup is Done!! Check out your profile using 'VP' Command" )
            break
        elif moredetails == "N": 
            print("Ok.. Your Account is set. You can add those details later by using command 'UpdateProfiel'.")
            break
        elif moredetails == "Exit":
            print("Press Ctrl + C to exit")
            
        else:
            print("Hmm... Not familiar with this command Try Again.")
    clrscr()    
    maincontent(userinfo)

