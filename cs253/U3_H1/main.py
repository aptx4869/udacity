#-*-encoding:utf-8-*-
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

form="""
<form method="post">
    What is your birthday?
    <br>
    <lable> month
    <input type="text" name="month">
    </lable>
    <lable> day
    <input type="text" name="day">
    </lable>
    <lable> year
    <input type="text" name="year">
    </lable>
    <br>
    <br>
    <input type="submit">
</form>
"""
html_rot13="""
<!DOCTYPE html>
<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(data)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""

html_signup="""
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
          %(inval_name)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">
          %(inval_pass)s
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="%(verify)s">
          </td>
          <td class="error">
          %(inval_verify)s

          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
          %(inval_email)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

html_wellcom="""
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Signup</title>
  </head>

  <body>
    <h2>Welcome, %(username)s!</h2>
  </body>
</html>
"""

import string,cgi,re

import os

import webapp2

import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    #if len(password)>2:
    return PASS_RE.match(password)
    #else:
        #return False

def valid_email(email):
    return MAIL_RE.match(email)

class Rot13Handler(webapp2.RequestHandler):
    def rot13(self,data=''):
        data=data.encode('rot13')
        return cgi.escape(data,quote=True)

    def get(self):
        self.response.out.write(html_rot13 % {"data":""})

    def post(self):
        text = self.request.get("text")
        value=self.rot13(text)
        self.response.out.write(html_rot13 % {"data":value})

class FormTestHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
class TestHandler(webapp2.RequestHandler):
    def post(self):
        #q = self.request.get("q")
        #self.response.out.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        username,password,verify,email,inval_name,inval_pass,inval_verify,inval_email=('',)*8
        variable_dic=locals()
        self.response.out.write(html_signup % variable_dic)

    def post(self):
        inval_name,inval_pass,inval_email,inval_verify = '','','',''
        username = cgi.escape(self.request.get("username"),quote=True)
        password = cgi.escape(self.request.get("password"),quote=True)
        verify = cgi.escape(self.request.get("verify"),quote=True)
        email = cgi.escape(self.request.get("email"),quote=True)
        if not valid_username(username):
            inval_name='That&#39;s not a valid username.'
            username=''
        if not valid_password(password):
            inval_pass='That wasn&#39;t a valid password.'
            password=''
            verify=''
        elif password != verify:
            inval_verify='Your passwords didn&#39;t match.'
            password=''
            verify=''
        if email != '' and not valid_email(email):
            inval_email='That&#39;s not a valid email.'
            email=''
        variable_dic=locals()
        variable_count = len(variable_dic) / 2
        #username = cgi.escape(username,quote=True)
        #password = cgi.escape(password,quote=True)
        #verify = cgi.escape(verify,quote=True)
        #username = cgi.escape(username,quote=True)
        if (inval_name,inval_pass,inval_email,inval_verify) != ('',)*variable_count:
            #self.response.out.write(html_signup % {"inval_name":inval_name, "inval_pass":inval_pass, "inval_verify":inval_verify, "inval_email":inval_email})
            self.response.out.write(html_signup % variable_dic)
        else:
            self.redirect('/wellcom?name=%s' % (username))


class WellcomHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        self.response.out.write(html_wellcom % {'username':name})



class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw) 
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params) 

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw)) 

class BlogPage(Handler):

    def get(self):
        articals=db.GqlQuery("SELECT * FROM Artical ORDER BY created DESC LIMIT 11")
        articals=enumerate(articals)
        self.render("blog.html",enumerate_articals=articals) 

class ArtHandler(Handler):
    def get(self):
        path=self.request.path
        art_id=int(path[path.rfind('/')+1:])
        articals=db.GqlQuery("SELECT * FROM Artical WHERE art_id=%d" % art_id)
        articals=enumerate(articals)
        self.render("blog.html",enumerate_articals=articals) 
        #self.write(path)

class Artical(db.Model):
    art_id=db.IntegerProperty()
    subject=db.StringProperty(required=True)
    content=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)
    #url=db.LinkProperty(

class NewPost(Handler):

    def get(self):
        self.render("newpost.html")

    def post(self):
        try:
            artical=db.GqlQuery("SELECT * FROM Artical ORDER BY art_id DESC LIMIT 1")
            art_id=artical[0].art_id + 1
        except:
            art_id=1

        subject=self.request.get("subject")
        content=self.request.get("content")
        if subject and content:
            artical=Artical(art_id=art_id,subject=subject,content=content)
            artical.put()
            self.redirect('/blog/%d' % art_id)
        else:
            #error="标题、内容不能为空"
            error='must be subject and content'
            self.render("newpost.html",subject=subject,content=content,error=error)

#XXX The form input boxes must have the names 'subject' 
#and 'content' in order for the grading script to correctly
#post to them.
#Don't forget to escape your output! 
        

app = webapp2.WSGIApplication([('/blog', BlogPage),
                                ('/blog/newpost', NewPost),
                                ('/blog/\d+', ArtHandler),
                                ('/formtest', FormTestHandler),
                                ('/testform', TestHandler),
                                ('/rot13',Rot13Handler),
                                ('/sign_up',SignUpHandler),
                                ('/wellcom',WellcomHandler)],
                              debug=True)
