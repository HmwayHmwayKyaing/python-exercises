try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

    config = { 
            'description': 'My Project',
            'author': 'My Nmae',
            'url': 'URL to get it at .',
            'download_url': 'Where to download it .',
            'author-email': 'My email',
            'version': '0.1',
            'install_requires': ['noes'],
            'packages': ['NAME'],
            'scripts':[],
            'name': 'projectname'
            }

    setup(**config)

