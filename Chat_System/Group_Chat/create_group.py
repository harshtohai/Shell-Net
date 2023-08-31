from data import userpersona
from Chat_System.Group_Chat.chat_in_group import chatingroup
from error_handeling import error_handel


# @error_handel
def createGroup(userinfo):
    groupname = input('Creating a New Group. Enter Group Name please.\n: ')
    from client import createGroup as CG
    from client import groupChatTo as GC

    groupid = CG(groupname,userinfo['Username'],userinfo)
    
    userpersona.find_one_and_update({'Username':userinfo['Username']},{'$set':{'GroupInfo':{groupname:groupid}}})
    userpersona.find_one_and_update({'Username':userinfo['Username']},{'$push':{'InInbox':groupname}})
    userinfo['InInbox'].append(groupname)
    userinfo['GroupInfo'].update({groupname:groupid})
    GC(userinfo['Username'],groupid,userinfo)