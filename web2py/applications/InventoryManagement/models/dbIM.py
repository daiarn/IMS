# -*- coding: utf-8 -*-
db.define_table(
    'user_admin',
    Field('name', requires=IS_NOT_EMPTY()),
    Field('surname', requires=IS_NOT_EMPTY()),
    Field('email', requires=IS_NOT_EMPTY()),
    Field('password', 'password', requires=IS_NOT_EMPTY()),
    Field('role', requires=IS_NOT_EMPTY()),
    )
