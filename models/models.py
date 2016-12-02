# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Circuitos(models.Model):
    _name = 'partes.circuitos'

    name = fields.Char(string="Nombre", required=True)
    lugar = fields.Char(string="Situación", required=True)


class Papis(models.Model):
    _name = 'partes.papis'

    fundido = fields.Boolean(string='Lámparas fundidas')
    iluminacion = fields.Boolean(string='Iluminación uniforme')
    danio = fields.Boolean(string='Daño en las unidades')
    limpieza = fields.Boolean(string='Limpieza')


class Mangas(models.Model):
    _name = 'partes.mangas'

    name = fields.Char(string="Nombre", required=True)
    luz = fields.Boolean(string='Estado de las luces')
    tela = fields.Boolean(string='Estado de la tela')


class Letreros(models.Model):
    _name = 'partes.letreros'


class Anomalias(models.Model):
    _name = 'partes.anomalias'

    descripcion = fields.Text(string="Descripción")


class Incidencias(models.Model):
    _name = 'partes.incidencias'

    descripcion = fields.Text(string="Descripción")


# class partes(models.Model):
#     _name = 'partes.partes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100