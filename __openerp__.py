# -*- coding: utf-8 -*-
{
    'name': "partes",

    'summary': """
        partes diarios de la ocupación TMA""",

    'description': """
        Módulo con los partes diarios a rellenar en la ocupación TMA:
            -Balizamiento
            -Grupos
            -etc
    """,

    'author': "Miguel González Canales",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
        'views/partebalizamiento.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}