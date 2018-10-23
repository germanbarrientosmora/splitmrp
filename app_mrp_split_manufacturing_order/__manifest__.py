{
    'name': 'MRP Split Manufacturing order',
    'summary': 'Split a MO in two with transferred pickings',
    'version': '12.0.7.24',
    'category': 'Manufacturing',
    'author': 'Sunpop.cn',
    'license': 'AGPL-3',
    'website': 'http://www.sunpop.cn',
    'depends': [
        'mrp',
        'stock',
    ],
    'data': [
         'views/mrp_production_views.xml',
         'wizard/mrp_product_produce_views.xml',
    ],
}
