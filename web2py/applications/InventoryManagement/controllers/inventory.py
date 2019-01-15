def inventory():
    user = auth.user
    comp = get_user_company(user)
    membership = db(db.auth_membership.user_id == user.id).select().first()
    fields = (db.item.id, db.item.Name, db.item.Worth, db.item.Category, db.item.Status)
    headers = {'item.id': 'ID',
               'item.Name': 'Name',
               'item.Worth': 'Value (EUR)',
               'item.Category': 'Category',
               'item.Status': 'Status'}
    default_sort_order = [db.item.Name]
    form = SQLFORM.grid(db.item.company_id == comp.id, create=False, fields=fields, headers=headers,
                        orderby=default_sort_order, maxtextlength=64, paginate=25,
                        editable=True, deletable=auth.has_membership('ROLE_ADMIN'))
    return dict(user=user, company=comp, form=form, membership=membership)


def inventoryInUse():
    user = auth.user
    comp = get_user_company(user)
    membership = db(db.auth_membership.user_id == user.id).select().first()
    rows = db((db.item.Status == 'Taken')&(db.item.company_id == comp.id)).select()
    return dict(user=user, company=comp, rows=rows, membership=membership)


def addItem():
    form=SQLFORM(db.item)
    user = auth.user
    comp = get_user_company(user)
    membership = db(db.auth_membership.user_id == user.id).select().first()
    if form.process().accepted:
        new_item = db(db.item).select().last()
        db(db.item.id == new_item.id).update(company_id=comp.id)
        if new_item.Status == 'Taken':
            db(db.item.id == new_item.id).update(Taken=1)
    return dict(form=form, user=user, company=comp, membership=membership)


def removeItem():
    user = auth.user
    comp = get_user_company(user)

    return dict(user=user, company=comp)


def add_category():
    user = auth.user
    company = get_user_company(user)
    membership = db(db.auth_membership.user_id == user.id).select().first()
    form = SQLFORM(db.category).process()
    return locals()


def edit_item():
    user = auth.user
    company = get_user_company(user)
    membership = db(db.auth_membership.user_id == user.id).select().first()
    item = db.item(request.args(0, cast=int))
    form = SQLFORM(db.item, item)
    if form.process().accepted:
        if item.Status == 'Taken':
            new_count = int(float(item.Taken)) + 1
            db(db.item.id == item.id).update(Taken=new_count)
    return locals()


@auth.requires_login()
def get_user_company(user):
    company = db(user.company_id == db.company.id).select().first()
    return company
