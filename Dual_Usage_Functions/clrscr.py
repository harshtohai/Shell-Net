import os
from error_handeling import error_handel


@error_handel
def clrscr():
    if os.name == 'posix':
        os.system('clear')

    elif os.name == 'nt':
        os.system('cls')