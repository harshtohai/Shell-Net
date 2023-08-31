from data import userpersona
from error_handeling import error_handel


@error_handel
def joinGroup(userinfo):
    grouptojoin = input('Enter the Group Key you wanna join in. Or press q to exit\n:')
    if grouptojoin.isdigit() == True and len(grouptojoin) == 7:
        from client import joinGroup as jg
        
        try:
            groupid, groupname = jg(grouptojoin,userinfo['Username'],userinfo)
            userinfo['InInbox'].append(groupname)
            userinfo.update({'GroupInfo':{}})
            userinfo['GroupInfo'].update({groupname:groupid})
            userpersona.find_one_and_update({'Username':userinfo['Username']},{'$set':{'GroupInfo':{groupname:groupid}}})
            userpersona.find_one_and_update({'Username':userinfo['Username']},{'$push':{'InInbox':groupname}})
            from client import groupChatTo      
            groupChatTo(userinfo['Username'], groupid,userinfo)
        except Exception as e:
            print('Group Does not exists. Try Again')
            joinGroup(userinfo)
    elif grouptojoin == 'q':
        return
    else:
        print('Invalid key to enter. Try Again...')
        joinGroup(userinfo)