import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw) 
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params) 

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw)) 

    def escape_get(self, key):
        return jinja2.escape(self.request.get(key))
                
    def get_cookie(self, key, default=None):
        return self.request.cookies.get(key,default)

    def set_cookie(self,key):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers.add_header('Set-Cookie',key)
