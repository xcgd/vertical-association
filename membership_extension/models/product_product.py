# Copyright 2016 Antonio Espinosa <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    product_membership_category_id = fields.Many2one(
        string="Product membership category",
        comodel_name="membership.membership_category",
        compute="_compute_product_membership_category_id",
        readonly=False,
        store=True,
    )

    @api.depends("company_id")
    def _compute_product_membership_category_id(self):
        """Reset the Product Membership Category in case a different Company is
        set.
        """
        for record in self:
            if record.company_id and record.product_membership_category_id.company_id:
                if (
                    record.product_membership_category_id.company_id
                    != record.company_id
                ):
                    record.product_membership_category_id = False

    def _get_next_date(self, date, qty=1):
        self.ensure_one()
        return self.product_tmpl_id._get_next_date(date, qty=qty)
