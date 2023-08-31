from data import userpersona
from datetime import datetime
from error_handeling import error_handel


@error_handel
def uploadpost(userinfo):
    posttoadd = input("Whats in your mind?\n: ")
    userinfo['Posts'].append(posttoadd)
    gettingdate = datetime.now()
    currenttime = f"{gettingdate.month}/{gettingdate.day}"
    userinfo['Time'].append(currenttime)
    print('This done')
    userinfo['Likes'].append(0)
    print(userinfo)
    userpersona.update_one({'Username':userinfo['Username']}, {'$push': {'Posts': posttoadd}})
    userpersona.update_one({'Username':userinfo['Username']}, {'$push': {'Time': currenttime}})
    userpersona.update_one({'Username':userinfo['Username']}, {'$push': {'Likes': 0 }})

