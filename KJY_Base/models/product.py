# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import Warning

class Product(models.Model):
    _inherit = "product.product"
    _description = u"产品"

    no = fields.Char(string=u'产品编码')
    name = fields.Char(string=u'产品名称')
    units = fields.Char(string=u'计量单位')
    valid_period = fields.Char(string=u'保质期')
    pass_require = fields.Char(string=u'通关要求')
    storage_require = fields.Char(string=u'仓储要求')
    other_require = fields.Char(string=u'其它要求')
    category_id = fields.Many2one('product.category', string=u'产品类别',index=True)
    purchase = fields.Boolean(string=u'允许采购', default=True)
    customer_level = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], string=u'风险等级')



