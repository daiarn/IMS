def employee():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)
def addEmployee():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)
def removeEmployee():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)