from Main_three.main_body import maincontent
from data import userinfo
from Dual_Usage_Functions.clrscr import clrscr
from error_handeling import error_handel


userinfo = userinfo
@error_handel
def login(userpersona,NetworkTimeout):
    # try:
        userinfo = userpersona.find_one({'Username':input("Enter your Username: ")})
        def passwordcheck():
            if input("Enter your Password: ") == userinfo['Password']:
                userinfo.pop('_id')
                maincontent(userinfo)            
            else:
                print('Incorrect Password')
                passwordcheck()
        passwordcheck()
        clrscr()

    # except Exception as e:
        
        
    #     if type(e) is AttributeError:
    #         print(f'Unable to find the user.')
            
    #     elif type(e) is TimeoutError or NetworkTimeout:
    #         print(f'Check you internet connection')
    #         print(e)