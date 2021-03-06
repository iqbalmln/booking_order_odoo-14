# -*- coding: utf-8 -*-
{
    'name': "Booking Order",

    'summary': """
        Booking Order App with odoo-14""",

    'description': """
        Booking Order App with odoo-14
    """,

    'author': "Iqbal Maulana",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/service_teams_views.xml',
        'views/booking_order_views.xml',
        'views/work_order.xml',
        'views/menu.xml',
        'report/work_order_report.xml',
        'report/report.xml',
        'data/data.xml',
        'wizard/wizard_cancelled.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
