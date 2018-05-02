from setuptools import setup

setup(
    name='StockCrawler',
    version='0.1',
    author='ryanwcyin',
    author_email='ryanwcyin@gmail.com',
    packages=['StockCrawler', 'StockCrawler.tests'],
    license='LICENSE',
    description='Get the historical stock price from yahoo',

    long_description=open('README.txt').read(),
    install_requires=[
        'pandas',
    ],
)
