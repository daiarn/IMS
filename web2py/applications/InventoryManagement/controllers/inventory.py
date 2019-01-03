def inventory():
    user_email = auth.user.email
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user_email=user_email)


def inventoryInUse():
    user_email = auth.user.email
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user_email=user_email)


def addItem():
    user_email = auth.user.email
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user_email=user_email)


def removeItem():
    user_email = auth.user.email
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user_email=user_email)