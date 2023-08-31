from itertools import zip_longest
from error_handeling import error_handel


@error_handel
def viewfollowersandfollowing(userinfo):  
    lenoffollowers = len(str(len(userinfo['Followers'])))
    lenoffollowing = len(str(len(userinfo['Following'])))
    print(f'\┌{"─"*22}┐',end=''),print(f'┌{"─"*22}┐')
    print(f'│     Followers: {len(userinfo["Followers"])}{" "*int(15 - int(len("Followers")+int(lenoffollowers)))}│',end=''),
    print(f'│     Following: {len(userinfo["Following"])}{" "*int(15- int(len("Following")+int(lenoffollowing)))}│')
    print(f'├{"─"*22}┤',end=''),print(f'├{"─"*22}┤')

    for followersvalue, followingvalue in zip_longest(userinfo['Followers'],userinfo['Following'],fillvalue=''):
            
        print(f'│   @{followersvalue}{" "*int(18 - len(followersvalue))}│',end='') 
        if followingvalue != '':
            print(f'│   @{followingvalue}{" "*int(18 - len(followingvalue))}│')
        else:
            print(f'│{" "*22}│')
        print(f'│{"─"*22}│',end=''),print(f'│{"─"*22}│')
    print(f'└{"─"*22}┘',end=''),print(f'└{"─"*22}┘')    
    