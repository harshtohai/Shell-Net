from data import userpersona
from error_handeling import error_handel


# @error_handel
def changeindex(user,userinfo):
    try:
        userinfo['InInbox'].remove(user)
    except:
        pass
    userinfo['InInbox'].insert(0,user)
    userpersona.find_one_and_update({'Username':userinfo['Username']},{'$set':{'InInbox':userinfo['InInbox']}})