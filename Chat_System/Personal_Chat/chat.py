from data import userpersona
from Chat_System.Chat_Functions.change_index import changeindex
from Chat_System.Chat_Functions.show_index import showindexes
from Dual_Usage_Functions.clrscr import clrscr
from error_handeling import error_handel


@error_handel
def chat(usertochat = False, userinfo = None):
    import client
    # print('clientimpoted')
    base = client.personalChatTo
    if usertochat is False:
        showindexes(userinfo)
        print('Who do you wanna talk to?\n')
        chatuser = input("Enter User's Username or Chat Index\n: ")
        clrscr()
        if chatuser.isdigit() == True :       
            print(userinfo)
            if len(userinfo['InInbox'][int(chatuser)]) in userinfo['GroupInfo'].keys():           
                changeindex(userinfo['InInbox'][int(chatuser)],userinfo)
                base = client.groupChatTo
                base(userinfo['Username'],userinfo['GroupInfo'][userinfo['InInbox'][int(chatuser)]],userinfo)
                
            else:
                changeindex(userinfo['InInbox'][int(chatuser)],userinfo)
                base(userinfo['Username'],userinfo['InInbox'][int(chatuser)],userinfo)
            
        elif chatuser in userinfo['InInbox']:
            
            if chatuser in userinfo['GroupInfo'].keys():
                changeindex(chatuser,userinfo)
                base = client.groupChatTo
                base(userinfo['Username'],userinfo['GroupInfo'][chatuser],userinfo)
            else:
                changeindex(chatuser,userinfo)
                base(userinfo['Username'],chatuser,userinfo)


        elif chatuser not in userinfo['InInbox'] and userpersona.find_one({'Username':chatuser}):
            userinfo['InInbox'].append(chatuser)
            changeindex(chatuser,userinfo)
            base(userinfo['Username'],chatuser,userinfo)
        else:
            print('Provided User does not match.')
        
    elif usertochat: 
        changeindex(usertochat,userinfo)
        userinfo['InInbox'].append(usertochat)
        base(userinfo['Username'],usertochat,userinfo)
    else:
        pass

