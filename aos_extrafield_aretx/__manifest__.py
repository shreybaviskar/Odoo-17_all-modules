{
    "name": "AOS Extra Invoice Fields (Aretex)",
    "summary": "Extra invoice fields and reminder settings (LR No., Transporter, Dispatched Through, Next due Kms)",
    "version": "17.0.1.0.0",
    "author": "areterix",
    "website": "http://www.yourcompany.com",
    "category": "Invoicing",
    "license": "LGPL-3",
    "depends": [
        "base",
        "account",
        "aretx_vehicle",
    ],
    "data": [
        "views/configuration_view.xml",
        "views/invoice_inherit_view.xml",
    ],
    "installable": True,
    "application": False,
}

