from error_handeling import error_handel


@error_handel
def authBodyHelp():
    print('#Auth Body Commands\n')
    print('Register \ R  -->  Create a new account.')
    print('Login    \ L  -->  Log into an existing Account.')
    print('Exit     \ E  -->  Exit the function.\n')
    print('Ctrl + C      -->  Always feel free to use Ctrl + C for hard exit.')

@error_handel
def mainBodyHelp():
    print('#Main Body Commands\n')
    print('ViewProfile   \ VP  -->  Have a look at your profile.')
    print('UpdateProfile \ UP  -->  Update your profile.')
    print('NewPost       \ NP  -->  Upload a Post.')
    print('MyPosts       \ MP  -->  See all your posts.')
    print('DelPost       \ DP  -->  Delete Post.')
    print('SearchUser    \ SU  -->  Search for a user.')
    print('CreateGroup   \ CG  -->  Create your own new Group')
    print('JoinGroup     \ JG  -->  Join a group by its unique ID')
    print('Chat          \ C   -->  Have a fun Chat with your friends.')
    print('Exit          \ E   -->  Exit the Shell Net.\n')
    print('Ctrl + C            -->  Always feel free to use Ctrl + C for hard exit.')

@error_handel
def searchBodyHelp():
    print('#Search Body Commands\n')
    print('User.ViewProfile / VP -->  View Searched users Profile.')
    print('User.ShowPosts   / SP -->  View Searched users Posts.')
    print('User.Follow      / F  -->  Follow the searched user.')
    print('User.UnFollow    / UF -->  UnFollow the searched user.')
    print('User.Followers   / FS -->  Show Followers of the searched user.')
    print('User.Followings  / FG -->  Show Followings of the searched user.')
    print('User.Chat        / UC -->  Chat with the Search User.')
    print('Search           / SU -->  Search for a new user.')
    print('Back             / B  -->  Go back to #Main Body.')
    print('Exit             / E  -->  Exit Shell Net')
    print('Ctrl + C              -->  Always feel free to use Ctrl + C for hard exit.')