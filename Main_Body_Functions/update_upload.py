from data import userpersona
from error_handeling import error_handel


@error_handel
def uploading_data(userinfo):
        userpersona.insert_one(userinfo)

@error_handel
def updating_user(key, value,userinfo):
    print(userpersona.update_one({'Username': userinfo.get('Username')}, {'$set': {key : value}}))
