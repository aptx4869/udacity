import webapp2
import jinja2
from database import *
from handler import Handler

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
        #content=jinja2.escape(self.request.get("content"))
        #subject=self.escape_get("subject")
        content=self.escape_get("content")
        if subject and content:
            artical=Artical(art_id=art_id,subject=subject,content=content)
            artical.put()
            self.redirect('/blog/%d' % art_id)
        else:
            error='must be subject and content'
            self.render("newpost.html",subject=subject,content=content,error=error)
