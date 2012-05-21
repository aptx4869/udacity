import hmac,string,random

SECRET='Three car peng peng'

def hash_str(s):
    return hmac.new(SECRET,s).hexdigest()

def make_secure_val(s,token=''):
    ts=str(s)+token
    return "%s|%s" % (s, hash_str(ts))

def keyname_from_cookie(cookie):
    _hash=hashval_form_cookie(cookie)
    return _hash.split('|')[0]

def hashval_form_cookie(cookie):
    return cookie.split(';')[0]

def check_secure_val(cookie,token=''):
    _hash=hashval_form_cookie(cookie)
    keyname=keyname_from_cookie(cookie)
    if _hash == make_secure_val(keyname,token):
        return keyname

def make_salt():
    return ''.join(random.choice(string.letters) for _ in range(5))

def salt_hash(password):
    salt=make_salt()
    return (hmac.new(salt,password).hexdigest(),salt)

def check_salted_pass(password,_hash,salt):
    the_hash=hmac.new(str(salt),str(password)).hexdigest()
    return _hash==the_hash
