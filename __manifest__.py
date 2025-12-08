{
    'name':"Pengelolaan Gudang",
    'version': '2.0.1',
    'category' : 'Inventory',
    'author': 'Moh. Nurhidayatush Shodiq',
    'depends': ['base', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/warehouse_location.xml',
        'views/w_product_views.xml',
        'views/stock_transaction.xml',
        'views/action_view.xml',
        'report/report.xml',
        'report/report_stock.xml',
        'views/menuItem.xml',
        
        
        ],
    'installable': True,
    'application': True
    
}