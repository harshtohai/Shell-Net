from Chat_System.Chat_Functions.change_index import changeindex
from Chat_System.Chat_Functions.show_index import showindexes
from error_handeling import error_handel


@error_handel
def chatingroup(groupid = None, userinfo  = None):
    from client import groupChatTo
    if groupid != None:
        changeindex(list(userinfo['GroupInfo'].keys())[list(userinfo['GroupInfo'].values()).index(groupid)])
        groupChatTo(userinfo['Username'],groupid)
    else:
        showindexes()
        groupinput = input('Enter Group name or Group Index')
        if groupinput.isdigit():
            try:
                groupFromIndex = userinfo['InInbox'][groupinput]
                changeindex(groupFromIndex)
                groupFromIndex = userinfo['GroupInfo'][groupFromIndex]             
                groupChatTo(userinfo['Username'],groupFromIndex)
            except IndexError:
                print('GroupIndex Out of Range. Try Again...')
                chatingroup()
        elif groupinput in userinfo['GroupInfo'].keys():
            changeindex(groupinput)
            groupChatTo(userinfo['Username'], userinfo['GroupInfo'][groupinput])
        elif groupinput == 'q':
            return
        else:
            print('The given Group does not match. Try Again...')
            chatingroup()