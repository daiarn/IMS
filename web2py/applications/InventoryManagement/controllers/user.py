# ---- example login page ----
def login():
    # response.flash = T("Hello World")
    # return dict(message=T('Welcome to web2py!'))
    auth.logout()
    return dict(form=auth.login())


def register():
    # response.flash = T("Hello World")
    # return dict(message=T('Welcome to web2py!'))
    # auth.logout()
    return dict(form=auth.register())


def company_registration():
    user = auth.user
    form = SQLFORM(db.company).process()
    return dict(form=form, user=user)
