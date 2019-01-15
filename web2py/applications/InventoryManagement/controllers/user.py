# ---- example login page ----
def login():
    # response.flash = T("Hello World")
    # return dict(message=T('Welcome to web2py!'))
    # auth.logout()
    return dict(form=auth.login())


def register():
    form = SQLFORM(db.auth_user, formstyle='divs')
    if form.process().accepted:
        user = db(db.auth_user).select().last()
        db.auth_membership.insert(
            user_id=user.id,
            group_id= 4
        )
    return dict(form=form)
    # return dict(form=auth.register())


def company_registration():
    user = auth.user
    form = SQLFORM(db.company)
    if form.process().accepted:
        company = db(db.company).select().last()
        db(db.auth_user.id == user.id).update(company_id=company.id)
    comp = get_user_company(user)
    return dict(form=form, user=user, company=comp)


def profile():
    form = auth.profile()
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp, form=form)


def company_profile():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


@auth.requires_login()
def get_user_company(user):
    print(user.company_id)
    company = db(user.company_id == db.company.id).select().first()
    return company

@auth.requires_login()
def log_out():
    auth.logout()