from odoo import models, fields,api, _

class warehouseProduct(models.Model):
    _name = 'warehouse.product'
    _description = 'Warehouse Product'
    _order = 'id desc'
    
    name = fields.Char(string = 'Nama Produk', required=True)
    sku = fields.Char(string = 'SKU', readonly=True)
    category = fields.Many2one("product.category", required=True)
    stock = fields.Integer(default = 0)
    location_id = fields.Many2one("warehouse.location", string="Lokasi Gudang")
    move_ids = fields.One2many("stock.transactions", "product_id")
    
    @api.model
    def create(self, vals_list):
        for vals in vals_list:
            product_name = vals.get("name")
            prefix = (product_name or '')[:3].upper()
            
            last = self.search([], order = 'id desc', limit=1)
            nextNum = (last.id + 1) if last else 1
            
            vals["sku"] = f"{prefix}-{str(nextNum).zfill(4)}"


        return super().create(vals)