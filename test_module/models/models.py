# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TestModule(models.Model):
    _name = 'test.module'

    name = fields.Char(string="Name")
