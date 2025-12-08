from odoo import fields, models, api, _

class warehouseLocation(models.Model):
    _name = "warehouse.location"
    _description = "Warehouse Location"
    
    name = fields.Char(string = "Lokasi Gudang", required=True)
    code = fields.Char(string = "Kode Gudang", required=True)
    capasity = fields.Integer(string = "Kapasitas", required=True, default = 0)
    
    