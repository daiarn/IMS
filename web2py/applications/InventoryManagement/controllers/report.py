def report():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))