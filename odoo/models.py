# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suscrptores(models.Model):
    _name = 'suscrptores.suscrptores'
    _description = 'suscrptores.suscrptores'

    Nombre = fields.Char()
    Apellidos = fields.Char()
    Fecha_Nacimiento = fields.Date
    Suscripcion = fields.Selection([('1','Normal'),('2','Gold'),('3','Premium')])

