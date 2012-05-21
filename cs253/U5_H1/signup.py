import string,re,random
import webapp2
import database
from handler import Handler
from secret import *

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return MAIL_RE.match(email)

def user_exist(username):
    user=database.get_one_user(username)
    return user.username==username if user else False
    
class SignUpHandler(Handler):
    def get(self):
        self.render("signup.html")
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def post(self):
        inval_name,inval_pass,inval_email,inval_verify = ('',)*4
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        if not valid_username(username):
            inval_name="That's not a valid username."
            username=''
        elif user_exist(username):
            inval_name="That user already exist."
            username=''
        if not valid_password(password):
            inval_pass="That wasn't a valid password."
            password=''
            verify=''
        elif password != verify:
            inval_verify="Your passwords didn't match."
            password=''
            verify=''
        if email != '' and not valid_email(email):
            inval_email="That's not a valid email."
            email=''

        if (inval_name,inval_pass,inval_email,inval_verify) != ('',)*4:
            self.render("signup.html", username=username,
                                    password=password,
                                    verify=verify,
                                    email=email,
                                    inval_name=inval_name,
                                    inval_pass=inval_pass,
                                    inval_verify=inval_verify,
                                    inval_email=inval_email)
        else:
            password,salt = salt_hash(password)
            token = make_salt()
            user= database.User(username=username,password=password,salt=salt,token=token)
            #print user.token
            #print user.username
            user.put()
            key=str('user_id=%s;Path=/' % make_secure_val(username,token))
            self.response.headers.add_header('Set-Cookie', key)
            #self.set_cookie(key)
            self.redirect('/wellcom')
