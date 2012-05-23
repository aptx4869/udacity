from google.appengine.ext import db
from google.appengine.api import memcache
from datetime import datetime

def blog_key(name = 'default'):
    return db.Key.from_path('blogs',name)

class Artical(db.Model):
    subject=db.StringProperty(required=True)
    content=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def cached_put(self):
        self.put()
        myid = self.key().id()
        memcache.set("Artical"+str(myid),[self])
        memcache.delete("Articals")
        return myid

    #def cached_query(myid,GqlString,update=False):
        #assert type(GqlString)==type("")
        #CachedQuery("Artical"

class User(db.Model):
    username=db.StringProperty(required=True)
    password=db.StringProperty(required=True)
    salt=db.StringProperty(required=True)
    token=db.StringProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)

    def cached_put(self):
        self.put()
        myid = self.key().id()
        #memcache.set("User"+str(myid),self)
        memcache.set(self.username + 'user',self)
        memcache.delete("Users")
        return myid

def get_user_token(username,newuser=False):
    user = get_one_user(username,newuser)
    return user.token if user else None

def get_user_name(username,newuser=False):
    user = get_one_user(username,newuser)
    return user.username if user else None

def get_one_user(username,newuser=False):
    assert type(username) in (type(u''),type(''))
    try:
        user = memcache.get(username + 'user')
        if user is None or newuser:
            users=db.GqlQuery("SELECT * FROM User \
                    WHERE username='%s'" % username)
            user = users.fetch(1)[0]
            memcache.set(username + 'user', user)
        return user
    except:
        return None


def CachedQuery(CacheKey,GqlString,update=False):
    assert type(CacheKey) == type('')
    assert type(GqlString) == type('')
    result = memcache.get(CacheKey)
    if result is None or update:
        result=db.GqlQuery(GqlString)
        result = list(result.fetch(1000))
        memcache.set(CacheKey,result)
        memcache.set(CacheKey+'_time',datetime.now())
    return result

def GetCacheTime(CacheKey):
    return memcache.get(CacheKey + "_time")

