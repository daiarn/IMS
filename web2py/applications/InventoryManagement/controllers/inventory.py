def inventory():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


def inventoryInUse():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


def addItem():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


def removeItem():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


@auth.requires_login()
def get_user_company(user):
    company = db(user.company_id == db.company.id).select().first()
    return company
