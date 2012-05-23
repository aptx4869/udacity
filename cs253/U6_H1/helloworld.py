import webapp2

class Hellworld(webapp2.RequestHandler):
    def get(self):
        print 'Content-Type: text/plain'
        print ''
        print 'Hello,Udacity!'
