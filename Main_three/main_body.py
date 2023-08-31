from Main_Body_Functions.update_profile import updateprofile
from Main_Body_Functions.upload_post import uploadpost
from Main_Body_Functions.del_post import delpost
from Dual_Usage_Functions.view_profile import viewprofile
from Dual_Usage_Functions.clrscr import clrscr
from Dual_Usage_Functions.show_posts import showposts
from Search_Body_Functions.view_followers_following import viewfollowersandfollowing
from Chat_System.Group_Chat.create_group import createGroup
from Chat_System.Group_Chat.join_group import joinGroup
from Chat_System.Personal_Chat.chat import chat
from Main_three.search_body import searchinguser
from Help.help import mainBodyHelp


def maincontent(userinfo):
    print('#Main Body')
    while True:
        maininput = input()
        clrscr()
        match maininput:
            case 'UpdateProfile' | 'UP':
                updateprofile(userinfo)
            case 'ViewProfile' | 'VP':
                viewprofile(True,userinfo)
            case 'User.Followers' | 'User.Followings' | 'FS' | 'FG':
                    viewfollowersandfollowing(userinfo)
            case 'NewPost' | 'NP':
                uploadpost(userinfo)
            case 'MyPosts' | 'MP':
                showposts(userinfo,userinfo['Username'])
            case 'DelPost' | 'DP':
                delpost(userinfo)
            case 'CreateGroup' | 'CG':
                createGroup(userinfo)
            case 'JoinGroup' | 'JG':
                joinGroup(userinfo)
            case 'Chat' | 'C':
                chat(usertochat= False, userinfo=userinfo)
            case 'SearchUser' | 'SU':
                searchinguser(userinfo)
            case 'Exit' | 'E':
                print("Press Ctrl + C to exit")
            case 'help':
                mainBodyHelp()
            case _:
                print("#Main Body | Invalid command. Try again... use 'help' ")
