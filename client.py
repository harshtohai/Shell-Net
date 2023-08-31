import socket 
import threading
import time
import winsound
from rich.console import Console
from error_handeling import error_handel
from Chat_System.Chat_Functions.share_post import sendpost


CONN = ('192.168.56.1',1234)
console = Console()
@error_handel
def sendingToServer(messagetosend):
    server.send(str(messagetosend).encode('utf-8'))   
@error_handel         
def closeclient():
    server.send('<~CloseClient~>'.encode('utf-8'))
    server.close()
@error_handel
def servercon(userfrom,userto):
    global server
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((CONN))
    sendingToServer(userfrom)
    time.sleep(0.1)
    sendingToServer(userto)

@error_handel
def groupcommands(messagetosend,groupto,username):
    match messagetosend:
        case '/GroupInfo' | '/GroupMembers' | '/GI' | '/GM':
            sendingToServer(f'<~GroupInfo~><~>{groupto}<~>{username}<~>{messagetosend}')
        case '/GI' | '/GM':
            sendingToServer(f'<~GroupInfo~><~>{groupto}<~>{username}<~>{messagetosend}')
        case '/help' | '/h':
            print('/GroupInfo    \ /GI -->  This Command is shows overview of the group')
            print('/GroupMembers \ /GM -->  This Command is to check see all the members of the group.')
            print('/SendPost     \ /SP -->  This Command is to share a post by its index eg. "/SendPost 1" by default the index is your last post.')
        case _: 
            print('Invalid Command. use /help to see commands')

@error_handel
def recieveMessage(userfrom):
    
    while True: 
        try:  
            message = server.recv(1024).decode('utf-8')
            if message[0:2] == '->':
                print(message[2:])
            elif message.__contains__(':') == True:
                if message.__contains__(f'@{userfrom}'):
                    winsound.MessageBeep(1)
                    pass
                print(message)
            
            else:
                return message
        except Exception as e:
            print(e)
            server.close()
            break

@error_handel
def personalChatTo(userfrom,userto,userinfo):
    servercon(userfrom,userto)
    sendingToServer(f'<~Retrive~><~><P><~>{userto}')
    reciecvingMessagethread = threading.Thread(target=recieveMessage,args= [userfrom])
    reciecvingMessagethread.start()
    while True:
        try:
            messagetosend = input()
            if messagetosend == 'q':
                closeclient()
                return
            elif messagetosend != '' and messagetosend[0] == '/':
                if messagetosend.split(' ')[0] == '/SendPost' or 'SP' and len(messagetosend.split(' ')) < 2:
                    userto = f'<P><~>{userto}<~>{userfrom}<~>'
                    sendpost(sendingToServer,messagetosend,userfrom,userto,userinfo,delay= 0.1)
                    sendpost(print,messagetosend,userfrom,'',userinfo,delay=0)
                else:
                    pass
            else:
                message = f'<P><~>{userto}<~>{userfrom}<~>{messagetosend}'
                sendingToServer(message)
                console.print(f'[green]{userfrom}:[/green] {messagetosend}',soft_wrap=True)
        except KeyboardInterrupt:
            closeclient()
        
            return
        except Exception as e:
            print(e)
            return
# personalChatTo('test','test','-')
# @error_handel
def groupChatTo(userfrom,groupto,userinfo):
    sendingToServer(f'<~Retrive~><~><G><~>{groupto}')
    reciecvingMessagethread = threading.Thread(target=recieveMessage, args= [userfrom])
    reciecvingMessagethread.start()
    while True:
        try:
            messagetosend = input()
            if messagetosend == 'q':
                closeclient()
                return
            elif messagetosend != '' and messagetosend[0] == '/' and messagetosend.split(' ')[0] == '/SendPost':
                if messagetosend.split(' ')[0] == '/SendPost' or 'SP' and len(messagetosend.split(' ')) < 2:                
                    userto = f'<G><~>{groupto}<~>{userfrom}<~>'
                    sendpost(sendingToServer,messagetosend,userfrom,userto,userinfo,delay= 0.1)
                    sendpost(print,messagetosend,userfrom,'',userinfo,delay=0)
                
            elif messagetosend[0] == '/':
                groupcommands(messagetosend,groupto,userfrom)

            else:
                print(f"{userfrom}: {messagetosend}")
                messagetosend = f'<G><~>{groupto}<~>{userfrom}<~>{messagetosend}'
                sendingToServer(messagetosend)

        except KeyboardInterrupt:
            closeclient()

        except:
            return

# @error_handel
def createGroup(groupname,username,userinfo):
    servercon(username,groupname)
    sendingToServer(f'<~Create~><~>{groupname}<~>{username}')
    groupid = server.recv(1024).decode('utf-8')
    print(groupid)
    return groupid

@error_handel
def joinGroup(groupname,username,userinfo):
    servercon(username,groupname)
    server.send(f'<~JoinGroup~><~>{groupname}<~>{username}'.encode('utf-8'))
    response = server.recv(1024).decode('utf-8')
    if response != 'None':
        response = response.split('<~>')
        # groupChatTo(username,response[0],userinfo)
        return response[0],response[1]
    else:
        return None
