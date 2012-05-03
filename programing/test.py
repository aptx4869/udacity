import string,cgi,re
before='abcdefghijklmnopqrstuvwxyz'
after=before[13:]+before[:13]
before+=before.upper()
after+=after.upper()
table = string.maketrans(after,before)
data='i hate it++!<$'
data=data.translate(table)
#print after
#print before
print cgi.escape(data,quote=True)
#cevag 'v ungr vg'.genafyngr(gnoyr)
print 'i hate it++!<$'.encode('rot13')
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return MAIL_RE.match(email)

def post(username,password,verify,email):
    inval_name,inval_pass,inval_email,pass_nomatch = '','','',''
    #username = self.request.get("unsername")
    #password = self.request.get("password")
    #verify = self.request.get("verify")
    #email = self.request.get("email")
    if not valid_username(username):
        inval_name='That&#39;s not a valid username.'
    if not valid_password(username):
        inval_pass='That wasn&#39;t a valid password.'
    elif password != verify:
        pass_nomatch='Your passwords didn&#39;t match.'
    if email != '' and not valid_email(email):
        inval_email='That&#39;s not a valid email.'
    write_dic=locals()
    if (inval_name,inval_pass,inval_email,pass_nomatch) != ('',)*4:
        #self.response.out.write(html_signup % {"inval_name":inval_name, "inval_pass":inval_pass, "pass_nomatch":pass_nomatch, "inval_email":inval_email})
        print inval_name,inval_pass,inval_email,pass_nomatch
        #print locals() 
    else:
        print write_dic
        print 'yes'
        #self.redirect('/wellcom?name=%s' % (name))

post('uui','pass','pass','solia1984@gmail.com')
print valid_email('solia1984@gmail.com').__str__
