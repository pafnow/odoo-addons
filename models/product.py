# Copyright 2020 Pafnow

from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    uom_weight = fields.Float('Weight', digits='Stock Weight', compute='_compute_uom_weight', inverse='_set_uom_weight')
    #uom_weight_id = fields.Many2one('uom.uom', 'Weight Unit of Measure', default=_get_default_weight_uom, required=True, help="Default unit of measure used for weight.")

    @api.depends('weight', 'uom_weight_id.factor')
    def _compute_uom_weight(self):
        for record in self:
            record.uom_weight = record.weight * record.uom_weight_id.factor

    def _set_uom_weight(self):
        for record in self:
            record.weight = record.uom_weight * record.uom_weight_id.factor_inv


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    uom_weight = fields.Float('Weight', digits='Stock Weight', compute='_compute_uom_weight', inverse='_set_uom_weight')
    uom_weight_id = fields.Many2one('uom.uom', 'Weight Unit of Measure', default=lambda self: self._get_weight_uom_id_from_ir_config_parameter(),
                                    domain="[('category_id.measure_type', '=', 'weight')]", required=True, help="Default unit of measure used for weight.")

    @api.depends('weight', 'uom_weight_id.factor')
    def _compute_uom_weight(self):
        for record in self:
            record.uom_weight = record.weight * record.uom_weight_id.factor

    def _set_uom_weight(self):
        for record in self:
            record.weight = record.uom_weight * record.uom_weight_id.factor_inv
