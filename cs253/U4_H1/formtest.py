import webapp2

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

class FormTestHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
