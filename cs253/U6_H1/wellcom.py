import webapp2
import database
import time
from handler import Handler
from secret import *

class WellcomHandler(Handler):

    def get(self):
        if self.username is not None:
            self.render("wellcom.html", username=self.username)
            #time.sleep(5.5)
            self.redirect('/blog')
        else:
            self.render("dont_cheat.html")
