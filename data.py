from pymongo.errors import ConfigurationError
from pymongo import MongoClient
from sys import exit

#This is Mongo Data and some instances of data
#
#

#Data Structure View
'''
userinfo = {
    'Name':'Jake',
    'Username':'JackMe',
    'Emailid':'jacking@famousmail.com',
    'Password':'********',
    'DOB':'2009/04/30',
    'Gender':'sus',
    'Bio':'This jacks hammer jack',
    'Field': 'Dev',
    'Posts': ['Poster','ok posting'],
    'Time':['8/22','9/22'],
    'Likes':[2,0],
    'Followers':['Jack2'],
    'Following':['Jack2'],
    'InInbox':['Jack2'],
    'NickNames':['Alone me'],
    'GroupInfo':{'Jack2':'358609'}

}
'''
try:
    connection_string = f""
    mongoclient = MongoClient(connection_string)
    shellnetdatabase = mongoclient.ShellNetDatabase
    userpersona = shellnetdatabase.UserPersona
except Exception as e:
    if type(e) == ConfigurationError:
        print('Internet connectivity error')
        exit()
        
registerlist = ['Name', 'Username', 'Emailid', 'Password','DOB','Field']
userinfo = {
    'Name':'harsh', 
        'Username':'', 
        'Emailid':'', 
        'Password':'', 
        'DOB':'', 
        'Gender':'', 
        'Bio':'',
        'Field':'',
        'Posts':[],
        'Time':[],
        'Likes':[10],
        'Followers':[],
        'Following':[],
        'InInbox':[],
        'NickNames':[],
        'GroupInfo':{}
}

searcheduser = {}
remainders = ['Bio','Gender']
allvar = registerlist+remainders+['Posts','Followers','Following','Likes']
ittrationForSearchedUser = ['Name','Username', 'Bio', 'DOB','Gender', 'Field','Posts','Followers','Following','Likes']

if __name__ == '__main__':
    from Main_three.Auth.auth_body import shellNet_starter
    shellNet_starter()