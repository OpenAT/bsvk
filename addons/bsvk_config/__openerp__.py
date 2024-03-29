# -*- coding: utf-8 -*-

{
    'name': 'bsvk_config',
    'summary': '''FS-Online bsvk instance configuration''',
    'description': '''
FS-Online Instance Configuration
================================

Customer configuration for the instance bsvk

- Default settings
- View modifications
- CSS
- Translations
    ''',
    'author': 'Michael Karrer (michael.karrer@datadialog.net), DataDialog',
    'version': '1.0',
    'website': 'https://www.datadialog.net',
    'installable': True,
    'depends': [
        'fsonline',
    ],
    'data': [
        'views/templates.xml',
        'views/snippet_options.xml',
    ],
}

    
