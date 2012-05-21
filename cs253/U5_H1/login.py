import webapp2
import database
from handler import Handler
from secret import *

class LoginHandler(Handler):
    def get(self):
        cookie=str('user_id=; Path=/')
        self.response.headers.add_header('Set-Cookie', cookie)
        self.render("login.html")

    def authorise(self,username,password):
        user=database.get_one_user(username)
        if user:
            salt=user.salt
            salted_password=user.password
            if check_salted_pass(password,salted_password,salt):
                return user

    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        user = self.authorise(username,password)
        if user is not None:
            token = make_salt()
            user.token = token
            user.put()
            cookie=str('user_id=%s; Path=/' % make_secure_val(username,token))
            self.response.headers.add_header('Set-Cookie', cookie)
            #self.set_cookie(cookie)
            self.redirect('/wellcom')
        else:
            error="login increct!"
            cookie=str('user_id=; Path=/')
            self.response.headers.add_header('Set-Cookie', cookie)
            self.render("login.html",error=error,username=username)
