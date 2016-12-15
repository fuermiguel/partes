# -*- coding: utf-8 -*-

from openerp import models, fields, api


class balizamiento(models.Model):
    _name = 'partes.balizamiento'
    _rec_name = 'numero_ot' #lo utilizo si no hay campo name

    numero_ot = fields.Integer()
    fecha = fields.Date('Fecha')
    id_sistema = fields.Many2one('partes.sistemas')
    id_papis = fields.One2many('partes.papisbalizamiento','id_papis', 'Papis')
    id_mangas = fields.One2many('partes.mangasbalizamiento','id_mangas', 'Mangas')
    id_circuitos =fields.One2many('partes.circuitosbalizamiento','id_circuitos', 'Circuitos')
    

class Sistemas(models.Model):
    _name = 'partes.sistemas'

    id_sistema = fields.One2many('partes.balizamiento', 'id_sistema')
    id_grupo = fields.Many2one('partes.grupos')


class Grupos(models.Model):
    _name = 'partes.grupos'
    _rec_name = 'nombreGrupo'

    nombreGrupo = fields.Char(string="NombreGrupo", required=True)
  #  id_grupo = fields.One2many('partes.sistemas', 'id_grupo')
    #id_circuito = fields.Many2one('partes.circuitos', 'id_circuito')
   # ids_circuito = fields.One2many('partes.circuitos', 'id_grupo','Grupos')

class CircuitosBalizamiento(models.Model):
    _name = 'partes.circuitosbalizamiento'
    _rec_name = 'nombreCircuito'
    
    #nombreCircuito = fields.Char(string="Nombre", required=True)
    nombreCircuito = fields.Many2one('partes.circuitos', 'Nombre Circuito')
    observaciones = fields.Text(string="Observaciones")
    id_grupo = fields.Many2one('partes.grupos', 'Grupo' )
    id_circuitos = fields.Many2one('partes.balizamiento')
    id_apagadas = fields.One2many('partes.apagadas','numeroApagada','Apagadas')
    id_reparadas = fields.Many2one('partes.reparadas')
    
    
class Circuitos(models.Model):
    _name = 'partes.circuitos'
    _rec_name = 'nombreCircuito'

    nombreCircuito = fields.Char(string="Nombre", required=True)
   

class Apagadas(models.Model):
    _name = 'partes.apagadas'

    numeroApagada = fields.Integer(string="Número apagada")
    #id_apagada = fields.Many2one('partes.circuitos', 'numeroApagada')


class Reparadas(models.Model):
    _name = 'partes.reparadas'

    numeroReparada = fields.Integer(string="Reparadas")
   # id_reparada = fields.One2many('partes.circuitos', 'id_reparadas')
    
    
class PapisBalizamiento(models.Model):
    _name = 'partes.papisbalizamiento'
    _rec_name = 'nombrePapi'
    
    nombrePapi = fields.Char(string="Nombre", required=True)
    papis = fields.Many2one('partes.papis')
    id_papis = fields.Many2one('partes.balizamiento')
    fundido = fields.Boolean(string='Lámparas fundidas')
    iluminacion = fields.Boolean(string='Iluminación uniforme')
    danio = fields.Boolean(string='Daño en las unidades')
    limpieza = fields.Boolean(string='Limpieza')


class Papis(models.Model):
    _name = 'partes.papis'
    _rec_name = 'nombrePapi'

    nombrePapi = fields.Char(string="Nombre", required=True)
      
    
class MangasBalizamiento(models.Model):
    _name = 'partes.mangasbalizamiento'
    _rec_name = 'mangas'
    
    #nombreManga = fields.Char(string="Nombre", required=True)
    mangas = fields.Many2one('partes.mangas')
    luz = fields.Boolean(string='Estado de las luces')
    tela = fields.Boolean(string='Estado de la tela')
    id_mangas = fields.Many2one('partes.balizamiento')


class Mangas(models.Model):
    _name = 'partes.mangas'
    _rec_name = 'nombreManga'
  
    nombreManga = fields.Char(string="Nombre", required=True)
   

class Letreros(models.Model):
    _name = 'partes.letreros'


class Anomalias(models.Model):
    _name = 'partes.anomalias'

    descripcion = fields.Text(string="Descripción")


class Incidencias(models.Model):
    _name = 'partes.incidencias'

    descripcion = fields.Text(string="Descripción")
