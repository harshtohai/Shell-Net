from textwrap import wrap
from rich.console import Console
from time import sleep
# from error_handeling import error_handel


console = Console()
def showposts(inputformyposts,username,print_or_send = console.print,userto = '',delay=0):
    if len(inputformyposts['Posts']) > 0:
        user = username
        usercount = len(user)
        timeindex = 0
        likes = 0
        for i in inputformyposts['Posts']:

            print_or_send('eneterd')
            print_or_send(f'{userto}┌{"─"*48}┐')
            sleep(delay)
            print_or_send(f'{userto}│   @{user}{" "*int(44 - usercount)}│')
            sleep(delay)
            print_or_send(f'{userto}│{" "*48}│')
            sleep(delay)
            wrapper = wrap(i,width=44, *'',initial_indent='│   ', subsequent_indent= '│   ' )
            for element in wrapper:
                elementlen = len(element)
                added = elementlen+1
                element = element + ' '*int(50- added)+'│'
                print_or_send(f'{userto}{element}')
                sleep(delay)
            print_or_send(f'{userto}│{" "*48}│')
            sleep(delay)
            times = inputformyposts['Time'][timeindex]
            addedfortimeandlikes = int(len(str(likes))+ len(str(times))+21  )
            likesandtime = f"│   Index: {str(likes)}   Date: {str(times)}{' ' * int(50 - addedfortimeandlikes)}│"
            print_or_send(f'{userto}{likesandtime}')
            sleep(delay)
            print_or_send(f'{userto}│{" "*48}│')
            sleep(delay)
            print_or_send(f'{userto}└{"─"*48}┘')
            sleep(delay)
            likes = likes + 1
            timeindex = timeindex + 1
    else: 
        print_or_send("There aren't any posts to show...")

