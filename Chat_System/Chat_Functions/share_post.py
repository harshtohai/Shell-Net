from Dual_Usage_Functions.show_posts import showposts
from error_handeling import error_handel
from rich.console import Console


console = Console()
@error_handel
def sendpost(sendtoserver, message ,username,userto,userinfo,delay):
    messagelist = message.split(' ')
    try:
        if len(messagelist)  == 1:
            post = userinfo['Posts'][-1]
            time = userinfo['Time'][-1]
            userinfo = {'Posts':[post],'Time':[time]}
            showposts(userinfo,username,sendtoserver,userto,delay= delay)
            pass
        elif len(messagelist) == 2:
            post = userinfo['Posts'][int(messagelist[1])]
            time = userinfo['Time'][int(messagelist[1])]
            userinfo = {'Posts':[post],'Time':[time]}
            showposts(userinfo,sendtoserver,username,sendtoserver,userto,delay= delay)
        else:
            pass
    except IndexError:
        console.print('[red]Post Index out of range.')