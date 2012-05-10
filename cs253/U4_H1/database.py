from google.appengine.ext import db

class Artical(db.Model):
    art_id=db.IntegerProperty()
    subject=db.StringProperty(required=True)
    content=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)

class User(db.Model):
    username=db.StringProperty(required=True)
    password=db.StringProperty(required=True)
    salt=db.StringProperty(required=True)
    token=db.StringProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)

def get_one_user(username):
    try:
        users=db.GqlQuery("SELECT * FROM User \
                WHERE username='%s'" % username)
        return users.fetch(1)[0]
    except:
        return None

