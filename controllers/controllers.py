# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderMsaifulA(http.Controller):
#     @http.route('/booking_order__msaiful_a/booking_order__msaiful_a/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order__msaiful_a/booking_order__msaiful_a/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order__msaiful_a.listing', {
#             'root': '/booking_order__msaiful_a/booking_order__msaiful_a',
#             'objects': http.request.env['booking_order__msaiful_a.booking_order__msaiful_a'].search([]),
#         })

#     @http.route('/booking_order__msaiful_a/booking_order__msaiful_a/objects/<model("booking_order__msaiful_a.booking_order__msaiful_a"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order__msaiful_a.object', {
#             'object': obj
#         })
