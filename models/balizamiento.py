from openerp import models, fields, api


class balizamiento(models.Model):
    _name = 'partes.balizamiento'
    _inherits = {'partes_circuitos': 'id_circuitos',
                 'partes_papis': 'id_papis',
                 'partes_mangas': 'id_mangas',
                 'partes_anomalias': 'id_anomalias',
                 'partes_incidencias': 'id_incidencias'}

    fecha = fields.date('Fecha')
    id_circuitos = fields.Many2many('partes_circuitos', string="circuito")
    id_papis = fields.Many2many('partes_papis', string="papis")
    id_magas = fields.Many2many('partes_mangas', string="mangas")
    id_anomalias = fields.Many2one('partes_anomalias', ondelete='set null',
                                     string="anomalias", index=True)
    id_incidencias = fields.Many2one('partes_incidencias', ondelete='set null',
                                     string="incidencias", index=True)