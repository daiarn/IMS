def employee():
    user = auth.user
    comp = get_user_company(user)
    membership = db(db.auth_membership.user_id == user.id).select().first()
    fields = (db.auth_user.first_name, db.auth_user.last_name, db.auth_user.email, db.auth_user.address, db.auth_user.city)
    headers = {'auth_user.first_name': 'First name',
               'auth_user.last_name': 'Last name',
               'auth_user.email': 'Email address',
               'auth_user.address': 'Address',
               'auth_user.city': 'City'}
    default_sort_order = [db.auth_user.last_name]
    if comp:
        form = SQLFORM.grid(db.auth_user.company_id == comp.id, fields=fields, headers=headers,
                            orderby=default_sort_order, maxtextlength=64, paginate=25, editable=False, create=False,
                            deletable=auth.has_membership('ROLE_ADMIN'))

    return dict(user=user, company=comp, form=form, membership=membership)


def addEmployee():
    form = SQLFORM(db.auth_user, formstyle='divs')
    user = auth.user
    comp = get_user_company(user)
    if form.process().accepted:
        new_user = db(db.auth_user).select().last()
        db.auth_membership.insert(
            user_id=new_user.id,
            group_id= 5
            )
        db(db.auth_user.id == new_user.id).update(company_id=comp.id)
    return dict(form=form, user=user, company=comp)


def removeEmployee():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


@auth.requires_login()
def get_user_company(user):
    company = db(user.company_id == db.company.id).select().first()
    return company
