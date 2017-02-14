
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'FancyRecommenderSystem',
    'author': 'FranciscoGutierrez',
    'url': 'https://github.com/FranciscoGutierrez/FancyRecommenderSystem',
    'download_url': 'https://github.com/FranciscoGutierrez/FancyRecommenderSystem',
    'author_email': 'francisco.gutierrez@cs.kuleuven.be',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['fancy-rs'],
    'scripts': [],
    'name': 'FancyRecommenderSystem'
}

setup(**config)
