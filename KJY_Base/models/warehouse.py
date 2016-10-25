# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import Warning

class Warehouse(models.Model):
    _name = "warehouse"
    _description = u"仓库"
    no = fields.Char(string=u'编号')
    name = fields.Char(string=u'名称')
    address = fields.Char(string=u'地址')
    manage_id = fields.Many2one('hr.employee', string=u'负责人',index=True)




