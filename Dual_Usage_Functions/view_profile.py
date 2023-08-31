from textwrap import wrap
from error_handeling import error_handel


@error_handel
def viewprofile(bool,userinfo,myinfo = None):
        print(f'{"─"*50}')
        print(f'{" "*20}User Info')
        print(f'{"─"*50}')
        print(f'┌{"─"*48}┐')
        print(f'│   @{userinfo["Username"]}{" "*int(44 - len(userinfo["Username"]))}│')
        print(f'│{" "*48}│')
        likes = len(userinfo['Likes'])
        geneder = userinfo['Gender']  
        name = userinfo['Name']
        field = userinfo['Field']  
        posts = len(userinfo['Posts'])
        dob = userinfo['DOB']  
        followers = len(userinfo['Followers'])
        following = len(userinfo['Following'])
        emailid = userinfo['Emailid']  
        # added variables


        addedforpostsandlikes = int(len(str(likes))+ len(str(posts))+22+int(27-int(13+len(str(posts)))) )
        adedforemailid = int(len(str(emailid))+14)      
        addedfornameandfiled = int(len(str(name))+ len(str(field))+21+int(27-int(12+len(str(name)))) )
        addedfordobandgender = int(len(str(dob))+ len(str(geneder))+21 +int(27-int(11+len(str(dob)))) )
        addedforfollowersandfollowing = int(len(str(followers))+ len(str(following))+30+ int(27-int(17+len(str(followers)))) )


        print(f"│   Name: {str(name)}{' '*int(30-int(12+int(len(str(name)))))}Field: {str(field)}{' ' * int(50 - addedfornameandfiled)}│")
        print(f"│   DOB: {str(dob)}{' '*int(30-int(11+len(str(dob))))}Gender: {str(geneder)}{' ' * int(50 - addedfordobandgender)}│")
        if bool:
            print(f"│   EmailId: {str(emailid)}{' ' * int(50 - adedforemailid)}│")

        print(f"│   Posts: {str(posts)}{' '*int(30-int(13+len(str(posts))))}Likes: {str(likes)}{' ' * int(50 - addedforpostsandlikes)}│")
        print(f"│   Followers: {str(followers)}{' '*int(30-int(17+len(str(followers))))}Following: {str(following)}{' ' * int(50 - addedforfollowersandfollowing)}│")
        if bool == False:
            z = 0
            for i in userinfo.get('Following'):
                    for j in myinfo.get('Following'):
                            if i == j:
                                    z = z+1
                            else:
                                    pass
            addedForMutualFriends =  int(len(str(z))+ len(str(following))+20 )
            print(f"│   Mutual Friends: {str(z)}{' ' * int(50 - addedForMutualFriends)}│")
        
        wrapper = wrap(userinfo['Bio'],width=44, *'',initial_indent='', subsequent_indent= '│         ' )
        for element in wrapper:
            elementlen = len(element)
            added = elementlen+1
            element = f"│   Bio: {element + ' '*int(50- added)+'│'}"
            print(element)
     
        print(f'│{" "*48}│')
        print(f'└{"─"*48}┘')
        print(f'{"─"*50}\n')