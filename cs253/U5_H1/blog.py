import webapp2
import jinja2
from database import *
from handler import Handler

class BlogPage(Handler):

    def get(self):
        articals=db.GqlQuery("SELECT * FROM Artical ORDER BY created DESC LIMIT 11")
        articals=enumerate(articals)
        self.render("blog.html",enumerate_articals=articals) 


class jsonBlogPage(Handler):
    def get_art_dict(self, artical):
        """return a dict of a artical"""
        return {"content":artical.content,
                "created": artical.created.ctime(),
                "last_modified": artical.created.ctime(), #XXX
                "subject": artical.subject}

    def get(self):
        articals=db.GqlQuery("SELECT * FROM Artical ORDER BY created DESC LIMIT 11")
        result=[]
        for art in articals:
            result.append(self.get_art_dict(art))

        #self.response.out.write(result) 
        self.jsonAPI(result)


class ArtHandler(Handler):
    def get(self):
        path=self.request.path
        art_id=int(path[path.rfind('/')+1:])
        articals=db.GqlQuery("SELECT * FROM Artical WHERE art_id=%d" % art_id)
        articals=enumerate(articals)
        self.render("blog.html",enumerate_articals=articals) 
        #self.write(path)


class jsonArtHandler(Handler):
    def get_art_dict(self, artical):
        """return a dict of a artical"""
        return {"content":artical.content,
                "created": artical.created.ctime(),
                "last_modified": artical.created.ctime(), #XXX
                "subject": artical.subject}
    def get(self):
        path=self.request.path
        #self.response.out.write(path[path.find('/',3)+1:path.rfind('.')-1])
        art_id=int(path[path.find('/',3)+1:path.rfind('.')])
        articals=db.GqlQuery("SELECT * FROM Artical WHERE art_id=%d" % art_id)
        art = articals[0]
        result=self.get_art_dict(art)
        self.jsonAPI(result)


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
