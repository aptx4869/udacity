import webapp2
from handler import Handler
class Rot13Handler(Handler):
    def rot13(self,data=''):
        return data.encode('rot13')

    def get(self):
        self.render("rot13.html")

    def post(self):
        text = self.request.get("text")
        self.render("rot13.html",data=self.rot13(text))
