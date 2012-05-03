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
import webapp2

def valid_day(day):
    #if type(day) == type(1):
    try:
        day = int(day)
        return day if day>0 and day<32 else None
    except:
        pass

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    for m in months:
        if month.lower() == m.lower():
            return m
    return None

def valid_year(year):
    try:
        int_year=int(year)
        return int_year if int_year > 1900 and int_year < 2020 else None
    except:
        pass
form="""
<form method="post">
    What is your birthday?
    <br>
    <lable> month
    <input type="text" name="month" value="%(mounth)s">
    </lable>
    <lable> day
    <input type="text" name="day" value="%(day)s">
    </lable>
    <lable> year
    <input type="text" name="year" value="%(year)s">
    </lable>
    <div style="color:red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def write_form(self,error="",mounth="",day="",year=""):
        self.response.out.write(form % {"error":error,
                                        "mounth":mounth,
                                        "day":day})

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(form)
        self.write_form()
class TestHandler(webapp2.RequestHandler):
    def post(self):
        #q = self.request.get("q")
        #self.response.out.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)
app = webapp2.WSGIApplication([('/', MainHandler),
                                ('/testform', TestHandler)],
                              debug=True)

    
