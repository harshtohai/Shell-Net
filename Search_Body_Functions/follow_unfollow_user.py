from data import userpersona
from error_handeling import error_handel


@error_handel
def followandunfollowuser(searcheduser,userinfo,condition='$push',):  
    if condition == '$push' and userinfo['Username'] not in searcheduser['Followers']:
        userinfo['Following'].append(searcheduser['Username'])
        searcheduser['Followers'].append(userinfo.get('Username'))
        userpersona.update_one({'Username':userinfo['Username']},{condition:{'Following':searcheduser['Username']}})
        userpersona.update_one({'Username':searcheduser['Username']},{condition:{'Followers':userinfo.get('Username')}})
   
    elif condition == '$pull' and userinfo['Username'] in searcheduser['Followers']:
        userinfo['Following'].remove(searcheduser['Username'])
        searcheduser['Followers'].remove(userinfo.get('Username'))
        userpersona.find_one_and_update({'Username':searcheduser['Username']},{condition:{'Followers':userinfo.get('Username')}})
        print('Followers complete')
        userpersona.find_one_and_update({'Username':userinfo['Username']},{condition:{'Following':searcheduser['Username']}})
        
    else:
        pass
    
