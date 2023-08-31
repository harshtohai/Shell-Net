from error_handeling import error_handel


@error_handel
def showindexes(userinfo):
    print(f'\n┌───┐',end=''),print(f'┌{"─"*13}┐')
    for index, value in enumerate(userinfo['InInbox']):
            
        print(f'│ {index} │',end='') 
        print(f'│ {value}{" "*int(10 - len(value))}  │')
        print(f'├{"─"*3}┤',end=''),print(f'├{"─"*13}┤')
    print(f'└{"─"*3}┘',end=''),print(f'└{"─"*13}┘')    