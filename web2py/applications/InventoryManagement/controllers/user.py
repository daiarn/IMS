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
    comp = get_user_company(user)
    return dict(form=form, user=user, company=comp)


def profile():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)

@auth.requires_login()
def get_user_company(user):
    company = db(user.id == db.company.admin_id).select().first()
    return company
