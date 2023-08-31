from data import userpersona
from error_handeling import error_handel


@error_handel
def delpost(userinfo):
    try: 
        print(userinfo)
        inputint = int(input('Enter the Index of the post you wanna delete.')) 
        userpersona.update_one({'Username':userinfo['Username']}, {'$pop': {'Posts':inputint}})
        userinfo['Posts'].pop(inputint = -1 if inputint == 0 else inputint)
        
    except Exception as e: 
        
        if type(e) == ValueError: 
            print('Must Enter an Integer')
            delpost()
        else:
            print('Check you Internet Connection and try again')
            
        pass
