import socket 
import threading
import random 
from sys import exit
import time


utf = 'utf-8'
allids = []
PersonalChatStructure = {}
GroupChatStructure={
    'GroupId': ['Messages']
}
userdatastructure = {'Username':{'ClientToken':'clientid','InboxIn':'chatin','InboxClients':{'Username':'Id'}},'test2':{'ClientToken':'','InboxIn':'','InboxClients':{}},'test':{'ClientToken':'','InboxIn':'','InboxClients':{}}}
activitystructure = {'Client':[],'ActiveUsers':[],'ActiveGroups':{'Groupid':[]}}
GroupStructure = {'AllGroups':{'GroupId':{'NameOfGroup':'GroupName','NameOfAdmin':'GroupAdmin','GroupdId':'GroupId','GroupMembers':[]}},'Clients':[]}

if __name__ == '__main__':
    CONN = ('192.168.56.1',1234)
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((CONN))
    server.listen()
    def generatingid(bool = False):
        range = [100000,999999]
        while True:
            if bool: 
                range = [1000000,9999999]
            theid = random.randint(range[0],range[1])
            print(theid)
            if theid in allids:
                continue
            else:
                allids.append(theid)
                return str(theid)
    
    def getParrsed(message,inte = 1):
        listmes = message.split('<~>')
        print(listmes)
        return str(listmes[inte])
    
    def createGroup(message,client,username):
        groupname = getParrsed(message,1)
        admin = getParrsed(message,2)
        groupId = generatingid(True)
        activitystructure['ActiveGroups'].update({groupId:[]})
        GroupStructure['AllGroups'].update({groupId:{'NameOfGroup':groupname,'NameOfAdmin':admin,'GroupdId':groupId,'GroupMembers':[username]}})
        GroupChatStructure.update({groupId:[]})
        userdatastructure[username]['InboxClients'].update({groupId:groupId})
        client.send(groupId.encode(utf))
        print(activitystructure)
    
    def groupinfo(message,client):
        cmd = getParrsed(message,3)
        groupto = getParrsed(message,1)
        username = getParrsed(message,2)

        match cmd:
            case '/GroupInfo':
                client.send(f"""\nGroupName: {GroupStructure['AllGroups'][groupto]['NameOfGroup']}\nGroupID: {groupto}\nTotalMembers: {len(GroupStructure['AllGroups'][groupto]['GroupMembers'])}\n""".encode(utf))
            case '/GroupMembers':    
                groupmembers = 'Group Members:\n'
                for member in GroupStructure['AllGroups'][groupto]['GroupMembers']:
                    groupmembers += f'@{member}\n'           
                client.send(groupmembers.encode(utf))
        
     
    def joinGroup(message,client,username):
        thekey = getParrsed(message,1)
        if thekey in activitystructure['ActiveGroups']:
            print('found it !')
            if username not in GroupStructure['AllGroups'][thekey]['GroupMembers']:
                GroupStructure['AllGroups'][thekey]['GroupMembers'].append(username)
            client.send(f'{thekey}<~>{GroupStructure["AllGroups"][thekey]["NameOfGroup"]}'.encode(utf))
            return True
        else:
            client.send('None'.encode(utf))
            return None
        
    
    def retrivechat(username,client,userto,group:bool = False):
        chatstructure = PersonalChatStructure
        print(chatstructure)
        if group:
            chatstructure = GroupChatStructure
            print(chatstructure)
        try:
            if group:
                theidkey = userto
            else:
                theidkey = userdatastructure[username]['InboxClients'][userto]
            print('Personal chat structure: \n')
            print(chatstructure)
            print(theidkey)
            print('couldnt find')
            print('couldnt find')
            print('couldnt find')
            print('couldnt find')
            print('couldnt find')
            for messages in chatstructure.get(theidkey):
                print('echo')
                time.sleep(0.1)
                client.send(f'->{messages}'.encode(utf))
            print('passed for loop')
        except BaseException as e:
            # print(e.with_traceback())
            # print_exc()
            pass

    
    def changeInInbox(client,InboxIn,username):
    
        try:
            activitystructure['ActiveGroups'][userdatastructure[username]['InboxIn']].remove(client)
        except:
            print('1fail')
            pass
        try:
            if client in activitystructure['ActiveGroups'][InboxIn]:
                pass
            else:
                activitystructure['ActiveGroups'][InboxIn].append(client)
                retrivechat(username,client,InboxIn,True)
        except:
            print('2fail')
            pass
        try:
            userdatastructure[username].update({'InboxIn':InboxIn})
        except:
            print('fail')
            pass

    
    def closeClient(client,username):
        try:
            activitystructure['ActiveGroups'][userdatastructure[username]['InboxIn']].remove(client)
        except:
            pass
        activitystructure['ActiveUsers'].remove(username)
        activitystructure['Client'].remove(client)
        userdatastructure[username]['InboxIn'] = ''
        userdatastructure[username]['ClientToken'] = ''
        print(activitystructure['ActiveUsers'])
        # client.close()  
        return
    
    
    def filluserdata(username,client):
        if username in userdatastructure:
            userdatastructure[username].update({'ClientToken':client})
            activitystructure['Client'].append(client)
            activitystructure['ActiveUsers'].append(username)
        else:
            userdatastructure.update({username:{'ClientToken':'','InboxIn':'','InboxClients':{}}})
    async def servercommands():
        while True:
            servercmd = input('')
            if servercmd == 'Server.Push.Data':
                pass
            elif servercmd == 'Server.Close':  
                exit()
                
    
    def brodcastToGroup(message,group,nottosend,username):
        GroupChatStructure[group].append(message)
        print(activitystructure)
        changeInInbox(nottosend,group,username)

        print(GroupChatStructure)
        for client in activitystructure['ActiveGroups'][group]:
            try:
                if nottosend == client:
                    pass
                else:
                    client.send(message.encode(utf))
            except Exception as e:
                print(e)
                activitystructure['ActiveGroups'][group].remove(client)
                activitystructure['ActiveUsers'].remove(client)
                activitystructure['Client'].remove(client)

            
    def brodcastPersonal(message,usertosend,client,username):
        print(activitystructure)
        changeInInbox(client,usertosend,username)
        try: 
            print(userdatastructure[username]['InboxClients'].keys())
            print(userdatastructure)
            print(usertosend)
            if usertosend in userdatastructure[username]['InboxClients'].keys():
                print('notgene')
                PersonalChatStructure[userdatastructure[username]['InboxClients'][usertosend]].append(message)
                print('not geeenen')
            else:
                thekey = generatingid()
                print(thekey)
                userdatastructure[username]['InboxClients'].update({usertosend:thekey})  
                userdatastructure[usertosend]['InboxClients'].update({username:thekey})  
                PersonalChatStructure.update({thekey:[]})        
                PersonalChatStructure[userdatastructure[username]['InboxClients'][usertosend]].append(message)

            if username == userdatastructure[usertosend]['InboxIn'] and userdatastructure[usertosend]['ClientToken'] != '':
                usertosend = activitystructure['Client'][activitystructure['ActiveUsers'].index(usertosend)]  
                usertosend.send(message.encode(utf))
        except Exception as e:
            # print(e.with_traceback(type(e)))
            print(e)
            pass
            # print(str(e.with_traceback(KeyError)))
        print(activitystructure)
        print(userdatastructure)
        print(PersonalChatStructure)

    
    def messageParser(message,client,username):
        parsedmessagelist = message.split('<~>')
        if parsedmessagelist[0] == '<P>':
            messagewithuser = f'{username}: {" ".join(parsedmessagelist[3:])}'
            brodcastPersonal(messagewithuser,parsedmessagelist[1],client,username)
            print('send to personal' )
        elif parsedmessagelist[0] == '<G>':
            print(activitystructure)
            activitystructure['ActiveGroups'][parsedmessagelist[1]].append(client)
            messagewithuser = f'{username}: {"".join(parsedmessagelist[3:]).strip()}'
            brodcastToGroup(messagewithuser,parsedmessagelist[1],client,username)

    
    def reciecvingMessage(client,username):
        print(client,username)
        while True:     
            try:            
                print('logged into whiletrue')
                message = client.recv(1024).decode(utf)
                print(message)
                
                if message == '<~CloseClient~>':
                    closeClient(client,username)
                    break
                elif getParrsed(message,0) == '<~GroupInfo~>':
                    groupinfo(message,client)

                elif getParrsed(message,0) == '<~Create~>':
                    createGroup(message,client,username)

                elif getParrsed(message,0) == '<~Retrive~>':

                    if getParrsed(message,1) == '<P>':
                        retrivechat(username,client,getParrsed(message,2))
                    else:
                        retrivechat(username,client,getParrsed(message,2),True)

                elif getParrsed(message,0) == '<~JoinGroup~>':
                        
                        if joinGroup(message,client,username) != None :
                            # retrivechat(username,client,getParrsed(message,1),True)
                            pass
                        else:
                            break
                else: 
                    print('send to parser')
                    messageParser(message,client,username)
            except Exception as e:
                print(e)
                closeClient(client,username)
                break

    
    def serverHandeling():
        while True:
                print('Server is listening for users....')
                client,addr = server.accept()    
                print(client)          
                username = client.recv(1024).decode(utf)
                print(username)
                try:
                    userto = client.recv(1024).decode(utf)
                    print(userto)
                except:
                    pass
                filluserdata(username,client)      
                if userdatastructure[username]['ClientToken'] != '':
                    reciecvingMessagethread = threading.Thread(target=reciecvingMessage,args=(client,username))
                    reciecvingMessagethread.start()
                    continue
                else:
                    print('skipped recieving')
                    continue
    serverHandeling()