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

import string,cgi,re
import formtest
import webapp2

import helloworld
import signup
import login
import logout
import wellcom
import blog
import rot13

class TestHandler(webapp2.RequestHandler):
    def post(self):
        #q = self.request.get("q")
        #self.response.out.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/blog', blog.BlogPage),
                                ('/blog/newpost', blog.NewPost),
                                ('/blog/\d+', blog.ArtHandler),
                                ('/formtest', formtest.FormTestHandler),
                                ('/testform', TestHandler),
                                ('/rot13',rot13.Rot13Handler),
                                ('/signup',signup.SignUpHandler),
                                ('/login',login.LoginHandler),
                                ('/logout',logout.LogoutHandler),
                                ('/helloworld',helloworld.Hellworld),
                                ('/wellcom',wellcom.WellcomHandler),
                                ('/',helloworld.Hellworld)],
                              debug=True)
