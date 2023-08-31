
from pymongo.errors import NetworkTimeout
from Main_three.Auth.register import register
from Main_three.Auth.login import login
from Help.help import authBodyHelp
from data import userinfo,userpersona
from Dual_Usage_Functions.clrscr import clrscr
from error_handeling import error_handel

@error_handel
def shellNet_starter():
    print("What do you wanna do? 'Register' or 'Login'")
    while True: 
        try:
            userinput = input()
            clrscr()
            match userinput:
                case "Register" | 'R':
                    register()
                case "Login" | 'L':
                    login(userpersona, NetworkTimeout)
                case "help" | 'R':
                    authBodyHelp()
                case "Exit" | 'E':
                    exit()
                case _:
                    print("\nTry Again... Remember I am case sensitive.\n")

        except KeyboardInterrupt: 
            print('Exiting Shell Net...')
            exit()