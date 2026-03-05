{
    'name': 'Sale Discount Amount',
    'version': '17.0.1.0',
    'depends': ['sale', 'account'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'reports/sale_report.xml',
        'reports/invoice_report.xml',
    ],
    'installable': True,
}
