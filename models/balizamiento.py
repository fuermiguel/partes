from openerp import models, fields, api


class balizamiento(models.Model):
    _name = 'partes.balizamiento'
    _inherits = {'partes.circuitos': 'id_circuitos',
                 'partes.papis': 'id_papis',
                 'partes.mangas': 'id_mangas',
                 'partes.anomalias': 'id_anomalias',
                 'partes.incidencias': 'id_incidencias'}

    #fecha = fields.date('Fecha')
    id_circuitos = fields.Many2many('partes.circuitos', string="circuito")
    id_papis = fields.Many2many('partes.papis', string="papis")
    id_magas = fields.Many2many('partes.mangas', string="mangas")
    id_anomalias = fields.Many2one('partes.anomalias', ondelete='set null',
                                     string="anomalias", index=True)
    id_incidencias = fields.Many2one('partes.incidencias', ondelete='set null',
                                     string="incidencias", index=True)