# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import datetime
# ---- example index page ----
@auth.requires_login()
def index():
    response.flash = T("Hello World")
    user = auth.user
    comp = get_user_company(user)
    membership = db(db.auth_membership.user_id == user.id).select().first()
    if comp:
        count_employees=db(db.auth_user.company_id==comp.id).count()
        count_items=db((db.item.id>0) & (db.item.company_id == comp.id)).count()
        count_items_taken = db((db.item.Status == 'Taken') & (db.item.company_id == comp.id)).count()
        rows = db((db.item.Status == 'Taken') & (db.item.company_id == comp.id)).select(limitby=(0, 5))
        rows_items=db(db.item.company_id == comp.id).select(limitby=(0, 10))
    else:
        count_employees = 1
        count_items = 0
        count_items_taken = 0
        rows = ""
        rows_items = ""
    today=datetime.datetime(request.now.year,request.now.month,request.now.day)
    count_active=db(db.auth_event.time_stamp==today).count()
    return dict(message=T('Welcome to web2py!'), user=user, company=comp, count_employees=count_employees,
                count_items=count_items, count_active=count_active, rows=rows, rows_items=rows_items,
                count_items_taken=count_items_taken, membership=membership)

# ---- API (example) -----
@auth.requires_login()
def get_user_company(user):
    company = db(user.company_id == db.company.id).select().first()
    return company

@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 


# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
