def inventory():
    user = auth.user
    comp = get_user_company(user)
    fields = (db.item.id, db.item.Name, db.item.Worth, db.item.Category, db.item.Status)
    headers = {'item.id': 'ID',
               'item.Name': 'Name',
               'item.Worth': 'Value (EUR)',
               'item.Category': 'Category',
               'item.Status': 'Status'}
    default_sort_order = [db.item.Name]
    form = SQLFORM.grid(db.item.company_id == comp.id, fields=fields, headers=headers, orderby=default_sort_order, maxtextlength=64, paginate=25)
    return dict(user=user, company=comp, form=form)


def inventoryInUse():
    user = auth.user
    comp = get_user_company(user)
    rows = db((db.item.Status == 'Taken')&(db.item.company_id == comp.id)).select()
    return dict(user=user, company=comp, rows=rows)


def addItem():
    form=SQLFORM(db.item)
    user = auth.user
    comp = get_user_company(user)
    if form.process().accepted:
        new_item = db(db.item).select().last()
        db(db.item.id == new_item.id).update(company_id=comp.id)
    return dict(form=form, user=user, company=comp)


def removeItem():
    user = auth.user
    comp = get_user_company(user)
    return dict(user=user, company=comp)


def add_category():
    user = auth.user
    company = get_user_company(user)
    form = SQLFORM(db.category).process()
    return locals()


def edit_item():
    user = auth.user
    company = get_user_company(user)
    item = db.item(request.args(0, cast=int))
    form = SQLFORM(db.item, item).process()
    return locals()


@auth.requires_login()
def get_user_company(user):
    company = db(user.company_id == db.company.id).select().first()
    return company
