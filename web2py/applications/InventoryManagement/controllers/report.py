def report():
    user_email = auth.user.email
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user_email=user_email)