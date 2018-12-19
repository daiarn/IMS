# ---- example login page ----
def login():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))
def register():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))
