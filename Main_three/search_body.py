from data import userpersona
from Dual_Usage_Functions.view_profile import viewprofile
from Search_Body_Functions.follow_unfollow_user import followandunfollowuser
from Search_Body_Functions.view_followers_following import viewfollowersandfollowing
from Dual_Usage_Functions.show_posts import showposts
from Dual_Usage_Functions.clrscr import clrscr
from Chat_System.Personal_Chat.chat import chat
from Help.help import searchBodyHelp
from error_handeling import error_handel

@error_handel
def searchuserinfo(searcheduser,userinfo):
            viewprofile(False,searcheduser,userinfo)
            print('#Search Body')
            while True: 
                inputforsearchuser = input()
                clrscr()
                match inputforsearchuser:
                    case 'User.ShowPosts' | 'SP':
                        showposts(searcheduser,searcheduser['Username'])
                    case 'User.ViewProfile' | 'VP':
                        viewprofile(False, searcheduser, userinfo)
                    case 'User.Follow' | 'F':
                        followandunfollowuser(searcheduser)
                    case 'User.UnFollow' | 'UF':
                        followandunfollowuser(searcheduser, '$pull')
                    case 'User.Followers' | 'User.Followings' | 'FS' | 'FG':
                        viewfollowersandfollowing(searcheduser)
                    case 'User.Chat' | 'UC':
                        chat(searcheduser['Username'],userinfo)
                    case 'Search' | 'SU':
                        searchinguser()
                    case 'Exit' | 'E':
                        print('Press Ctrl + C to Exit')
                    case 'Back' | 'B':
                        break
                    case 'help':
                        searchBodyHelp()
                    case _:
                        print('Not a Valid Command for Search Body')
                
def searchinguser(userinfo):
    userToFind = input('Enter the Username you wanna find.\n: ')
    try:
        searcheduser = userpersona.find_one({'Username':userToFind}).copy()
        searchuserinfo(searcheduser, userinfo)
    except:
        print('User not found. Try Again. ')

       