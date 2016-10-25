# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import Warning

class ResPartnerCustomer(models.Model):
    _inherit = "res.partner"
    _description = u"客户"

    business_license_no = fields.Char(string=u'营业执照', size=20)
    business_license_img = fields.Binary(string=u'营业执照图片')
    customer_category = fields.Selection([('A', '个人'), ('B', '公司')], string=u'客户类型')
    customer_level = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], string=u'客户评级')
    remark = fields.Char(string=u'客户审核备注')


