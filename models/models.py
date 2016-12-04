# -*- coding: utf-8 -*-

from openerp import models, fields, api


class balizamiento(models.Model):
    _name = 'partes.balizamiento'

    numero_ot = fields.Integer()
    #fecha = fields.date()
    id_sistema = fields.Many2one('partes.sistemas')
    id_papis = fields.Many2one('partes.papis')
    id_mangas = fields.Many2one('partes.mangas')
    

class Sistemas(models.Model):
    _name = 'partes.sistemas'

    id_sistema = fields.One2many('partes.balizamiento', 'id_sistema')
    id_grupo = fields.Many2one('partes.grupos')


class Grupos(models.Model):
    _name = 'partes.grupos'

    nombreGrupo = fields.Char(string="NombreGrupo", required=True)
    id_grupo = fields.One2many('partes.sistemas', 'id_grupo')
    id_circuito = fields.Many2one('partes.circuitos')


class Circuitos(models.Model):
    _name = 'partes.circuitos'

    nombreCircuito = fields.Char(string="NombreCircuito", required=True)
    observaciones = fields.Text(string="Observaciones")
    id_grupo_ = fields.One2many('partes.grupos', 'id_circuito')

    id_apagada = fields.Many2one('partes.apagadas')
    id_reparada = fields.Many2one('partes.reparadas')


class Apagadas(models.Model):
    _name = 'partes.apagadas'

    numeroApagada = fields.Integer(string="Apagadas")
    id_apagada_ = fields.One2many('partes.circuitos', 'id_apagada')


class Reparadas(models.Model):
    _name = 'partes.reparadas'

    numeroReparada = fields.Integer(string="Reparadas")
    id_reparada = fields.One2many('partes.circuitos', 'id_reparada')


class Papis(models.Model):
    _name = 'partes.papis'

    id_papis = fields.One2many('partes.balizamiento', 'id_papis')
    fundido = fields.Boolean(string='Lámparas fundidas')
    iluminacion = fields.Boolean(string='Iluminación uniforme')
    danio = fields.Boolean(string='Daño en las unidades')
    limpieza = fields.Boolean(string='Limpieza')


class Mangas(models.Model):
    _name = 'partes.mangas'

    id_mangas = fields.One2many('partes.balizamiento', 'id_mangas')
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
