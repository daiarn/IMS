def report():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


@auth.requires_login()
def get_user_company(user):
    company = db(user.id == db.company.admin_id).select().first()
    return company
