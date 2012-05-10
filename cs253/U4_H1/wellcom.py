import webapp2
import database
from handler import Handler
from secret import *

class WellcomHandler(Handler):
    def get_token(self, username):
        user=database.get_one_user(username)
        return user.token if user else 'invalid-token'

    def get(self):
        cookie=self.get_cookie('user_id')
        username=keyname_from_cookie(cookie)
        token=self.get_token(username)
        if check_secure_val(cookie,token):
            self.render("wellcom.html", username=username)
        else:
            self.render("dont_cheat.html")
