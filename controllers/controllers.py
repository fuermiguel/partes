# -*- coding: utf-8 -*-
from openerp import http

# class Partes(http.Controller):
#     @http.route('/partes/partes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partes/partes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partes.listing', {
#             'root': '/partes/partes',
#             'objects': http.request.env['partes.partes'].search([]),
#         })

#     @http.route('/partes/partes/objects/<model("partes.partes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partes.object', {
#             'object': obj
#         })