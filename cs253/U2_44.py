
def escape_html(s):
    s=s.replace('&','&amp;')
    s=s.replace('<','&lt;')
    s=s.replace('>','&gt;')
    s=s.replace('"','&quot;')
    return s

print escape_html('<p .>')
