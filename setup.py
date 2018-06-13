from setuptools import setup

setup(
    name = 'manga-scrapper',
    packages = ['manga-scrapper'],
    version = '0.1',
    description = 'Manga-scrapper is a small image scrapper based on BeautifulSoup4 and cfscrape',
    author = ['Daniel Montivero', 'Nils Gillmann'],
    author_email = ['danielelnuevo@hotmail.com', 'ng0@n0.is'],
    url = 'https://c.n0.is/gillmann/manga-scrapper',
    keywords = ['manga', 'scraping'],
    include_package_data = True,
    install_requires = ['cfscrape', 'BeautifulSoup']
)
