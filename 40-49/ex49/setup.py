try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'ex49',
    'author': 'BryJC',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'bryjc.projects@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts': [],
    'name': 'ex49'
}

setup(**config)
