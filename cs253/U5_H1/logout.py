import webapp2
import database
from handler import Handler
from secret import *

class LogoutHandler(Handler):

    def get_valid_user(self, cookie):
        username=keyname_from_cookie(cookie)
        user=database.get_one_user(username)
        if user:
            token=user.token
            if check_secure_val(cookie,token):
                return user

    def get(self):
        cookie=self.get_cookie('user_id')
        user = self.get_valid_user(cookie)
        if user:
            user.token='invalid'
            user.put()
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
        #key=str('user_id=; Path=/')
        #self.set_cookie(key)
        self.redirect('/signup')
