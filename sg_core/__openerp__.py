# -*- coding: utf-8 -*-
{
    'name': 'Core',
    'category': 'smartgo',
    'sequence': 10,
    'summary': 'SmartGo Core',
    'website': 'https://www.odoo.com/page/website-builder',
    'version': '1.0',
    'description': """
SmartGo Addons Core Modules
===========================

        """,
    'depends': ['web', 'web_editor', 'web_planner'],
    'installable': True,
    'data': [
        'views/res_users_view.xml',
    ],
    'application': False,
}
