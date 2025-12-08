from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class stockTransactions(models.Model):
    _name = "stock.transactions"
    _description = "Stock Transaction"
    
    product_id  = fields.Many2one("warehouse.product", string="Product")
    qty         = fields.Integer(string="qty", default = 0)
    move_type   = fields.Selection([("in", "Stock In"), ("out", "Stock Out")], required=True)
    date        = fields.Datetime(default = fields.Datetime.now)
    references  = fields.Char()
    
    @api.model
    def _extract_m2o_id(self, value):
        """Return Many2one ID from any Odoo command format."""
        if isinstance(value, int):
            return value
        
        if isinstance(value, list):
            # Case: [4, ID]
            if len(value) >= 2 and isinstance(value[1], int):
                return value[1]
            # Case: [6, False, [ID]]
            if len(value) >= 3 and isinstance(value[2], list):
                return value[2][0]
        
        if isinstance(value, dict):
            # auto-create record m2o
            rec = self.env["warehouse.product"].create(value)
            return rec.id
        
        return None
    
    @api.model
    def create(self, vals_list):
        for vals in vals_list:
            product_id = self._extract_m2o_id(vals.get("product_id"))
            if product_id:
                vals["product_id"] = product_id

            product = self.env["warehouse.product"].browse(product_id)
            qty = vals["qty"]
            
            if vals ["move_type"] == "in":
                if product.location_id and product.stock + qty > product.location_id.capasity:
                    raise ValidationError(f"Stok melebihi Kapasitas Gudang di {product.location_id.name}")
                product.stock += qty
            else:
                if product.stock < qty:
                    raise ValidationError("Stock Tidak Cukup")
                product.stock -= qty
        return super().create(vals)
