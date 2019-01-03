def report():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)