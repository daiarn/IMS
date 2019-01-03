def inventory():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)


def inventoryInUse():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)


def addItem():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)


def removeItem():
    user = auth.user
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'), user=user)