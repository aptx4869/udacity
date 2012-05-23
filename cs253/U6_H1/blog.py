import webapp2
import jinja2
import database
from handler import Handler
from datetime import datetime
from google.appengine.api import memcache

class FlushHandler(Handler):
    def get(self):
        memcache.flush_all()
        self.redirect('/')

class BlogPage(Handler):

    def get(self):
        articals=database.CachedQuery("Articals",
                "SELECT * FROM Artical ORDER BY created DESC LIMIT 11")
        cache_time = database.GetCacheTime("Articals")
        cache_time = cache_time if cache_time else datetime.now()
        timenow = datetime.now()
        delta_t=(timenow-cache_time).seconds
	query_time = "Queried %d second ago" %delta_t

        articals=enumerate(articals)
        self.render("blog.html",enumerate_articals=articals,query_time=query_time,username=self.username) 

class jsonBlogPage(Handler):
    def get_art_dict(self, artical):
        """return a dict of a artical"""
        return {"content":artical.content,
                "created": artical.created.ctime(),
                "last_modified": artical.last_modified.ctime(),
                "subject": artical.subject}

    def get(self):
        articals=database.CachedQuery("Articals",
                "SELECT * FROM Artical ORDER BY created DESC LIMIT 11")
        result=[]
        for art in articals:
            result.append(self.get_art_dict(art))

        self.jsonAPI(result)


class ArtHandler(Handler):
    def get(self):
        path=self.request.path
        art_id=path[path.rfind('/')+1:]   #XXX ugly
        key = "Artical" + art_id
        articals=database.CachedQuery(key,
                "SELECT * FROM Artical WHERE __key__=KEY('Artical', %s)" % art_id)
        cache_time = database.GetCacheTime(key)
        cache_time = cache_time if cache_time else datetime.now()
        timenow = datetime.now()
        delta_t=(timenow-cache_time).seconds
	query_time = "Queried %d second ago" %delta_t
        articals=enumerate(articals)
        self.render("artical.html",enumerate_articals=articals,query_time=query_time,username=self.username) 
        #self.write(path)


class jsonArtHandler(Handler):
    def get_art_dict(self, artical):
        """return a dict of a artical"""
        return {"content":artical.content,
                "created": artical.created.ctime(),
                "last_modified": artical.last_modified.ctime(),
                "subject": artical.subject}
    def get(self):
        path=self.request.path
        #self.response.out.write(path[path.find('/',3)+1:path.rfind('.')-1])
        art_id=int(path[path.find('/',3)+1:path.rfind('.')])
        key = "Artical" + str(art_id)
        articals=database.CachedQuery(key,
                "SELECT * FROM Artical WHERE __key__=KEY('Artical', %d)" % art_id)
        art = articals[0]
        result=self.get_art_dict(art)
        self.jsonAPI(result)


class NewPost(Handler):

    def get(self):
        self.render("newpost.html")

    def post(self):
        subject=self.request.get("subject")
        #content=jinja2.escape(self.request.get("content"))
        #subject=self.escape_get("subject")
        content=self.escape_get("content")
        if subject and content:
            artical=database.Artical(subject=subject,content=content)
            art_id = artical.cached_put()
            #art_id = artical.key().id()
            self.redirect('/blog/%d' % art_id)
        else:
            error='must be subject and content'
            self.render("newpost.html",subject=subject,content=content,error=error)
