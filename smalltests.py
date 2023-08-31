# I am providing this file to show you how rookie I am and how I test around things.
# 
# 


















# # import curses
# # print(f'{"-"*155}')
# # print(f'{" "*73} User Info')
# # print(f'{"-"*155}\n\n\n\n\n\n\n\n')
# # print(f'{"-"*155}')
# # print(curses.get_tabsize())

# import json
# # f='helloaaooa'
# import datetime
# import re
# import itertools
# userinfo = {'Name':'', 'Username':'', 'Emailid':'', 'Password':'', 'DOB':'', 'Gender':'', 'Bio':'','Field':'','Posts':[],'Time':[],'Likes':[10],'Followers':['hello','to','me'],'Following':['he'],'ChatUsers':[]}
# myinfo = {'Name':'', 'Username':'', 'Emailid':'', 'Password':'', 'DOB':'', 'Gender':'', 'Bio':'','Field':'','Posts':[],'Time':[],'Likes':[10],'Followers':['hel','to','me'],'Following':['this','is','something'],'ChatUsers':[]}
# # def checkingDOB():
                        
# #     registerinput = input(f"Enter your DOB Date of Birth eg 2022/12/01: ")
# #     try:
# #         datetime.datetime.strptime(registerinput,'%Y/%m/%d')
# #         print(registerinput)
# #         userinfo.update({'DOB':registerinput})
# #         # print('Okay this was true')
        
# #     except Exception as e:
# #         if type(e) == ValueError:
# #             print(e)
# #             print('Invalid Date or Format')  
# #             checkingDOB()
                           
# # checkingDOB()
# # z = 0
# # for i in userinfo.get('Followers'):
# #         for j in myinfo.get('Followers'):
# #                 if i == j:
# #                         print(i)
# #                         z = z+1
# #                 else:
# #                         pass
# # print(z)
# # lenoffollowers = len(str(len(userinfo['Followers'])))
# # lenoffollowing = len(str(len(userinfo['Following'])))
# # print(f'\n╭{"―"*22}╮',end=''),print(f'╭{"―"*22}╮')
# # print(f'│     Followers: {len(userinfo["Followers"])}{" "*int(15 - int(len("Followers")+int(lenoffollowers)))}│',end=''),
# # print(f'│     Following: {len(userinfo["Following"])}{" "*int(15- int(len("Following")+int(lenoffollowing)))}│')
# # print(f'│{"―"*22}│',end=''),print(f'│{"―"*22}│')

# # for followersvalue, followingvalue in itertools.zip_longest(userinfo['Followers'],userinfo['Following'],fillvalue=''):
        
# #     print(f'│   @{followersvalue}{" "*int(18 - len(followersvalue))}│',end='') 
# #     if followingvalue != '':
# #         print(f'│   @{followingvalue}{" "*int(18 - len(followingvalue))}│')
# #     else:
# #         print(f'│{" "*22}│')
# #     print(f'│{"―"*22}│',end=''),print(f'│{"―"*22}│')
# # print(f'╰{"―"*22}╯',end=''),print(f'╰{"―"*22}╯')    


# # for i,j in itertools.zip_longest(myinfo['Followers'],userinfo['Following'],fillvalue=''):
# #       print(i,j)


# group = {'GH':[],'hg':0}
# test = 'hello!no'
# test = [1,2]
# # test.
# try:
#     print(test+1)
#     print(test)
# except:
#     print(test)

# # testl = test.split('!')
# # print(' '.join(testl[0:]))
# # newtest = test.split('.')
# # test = ''.join(newtest[0])
# # # test.
# # if test.rfind('!') is False:
# #     print('not')
# # # 
# # test.re
# # group.update({'GH':test.split('!')[0]})
# # print(group)


# userdatastructure = {'h':{'h':'h','ClientId':'10','Groups':'groupin','ActiveClients':[10]}}
# serverdatastructure = {'Client':[10,],'ActiveUsers':['h',],'ActiveGroups':{'groupin':[10]}}
# client = 10
# print(serverdatastructure['ActiveGroups'][userdatastructure['h']['Groups']].remove(10))



# chatbase = {
#     'PersonalChat':
#     {
#         123:{'Harsh':'Hello','Name':'hello there'}
#     }
# }
# Severbase = {
#     'Harsh':{'Name':123,'Another':456},
#     'Name':{'Harsh':123,'Another':789}
# }

# ChatStructure = {
#     'Id':[]
# }

# # print(ChatStructure['Id'][0].)
# # ChatStructure.update()
# print(ChatStructure)


# def fun():
#     ChatStructure['Id'] = ''
#     print(ChatStructure)
# fun()
# print(ChatStructure)


# if '' in ChatStructure.keys():
#     print('itis')



# test = {'Id':{'2Id':"nothing"}}
# if 'nothing' in test['Id']:
#     print(test)

# import inspect
# inspect.getsource(input())

# test = 'hello there'

# print(test.find('h'))
# if test.find('h') is True:
#     print(test.find('h'))
userinfo = {'Name':'harsh', 'Username':'', 'Emailid':'', 'Password':'', 'DOB':'', 'Gender':'', 'Bio':'','Field':'','Posts':[],'Time':[],'Likes':[10],'Followers':[],'Following':[],'InInbox':['ahrsh','harsh'],'NickNames':[],'GroupInfo':{}}

# def showindexes():
#     print(f'\n╭―――╮',end=''),print(f'╭{"―"*13}╮')


#     for index, value in enumerate(userinfo['InInbox']):
            
#         print(f'│ {index} │',end='') 
#         print(f'│   {value}{" "*int(10 - len(value))}│')
#         print(f'│{"―"*3}│',end=''),print(f'│{"―"*13}│')
#     print(f'╰{"―"*3}╯',end=''),print(f'╰{"―"*13}╯')    
# showindexes()