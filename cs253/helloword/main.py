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
import webapp2,string,cgi,re
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

        #before='abcdefghijklmnopqrstuvwxyz'
        #after=before[13:]+before[:13]
        #before+=before.upper()
        #after+=after.upper()
        #table = string.maketrans(after,before)
        #v=data.translate( table )
        #print cgi.escape(data,quote=True)
        #return cgi.escape(data,quote=True)
        
    def get(self):
        self.response.out.write(html_rot13 % {"data":""})

    def post(self):
        text = self.request.get("text")
        value=self.rot13(text)
        self.response.out.write(html_rot13 % {"data":value})

class MainHandler(webapp2.RequestHandler):
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

app = webapp2.WSGIApplication([('/', MainHandler),
                                ('/testform', TestHandler),
                                ('/rot13',Rot13Handler),
                                ('/sign_up',SignUpHandler),
                                ('/wellcom',WellcomHandler)],
                              debug=True)
