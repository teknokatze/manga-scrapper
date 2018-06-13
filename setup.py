from setuptools import setup

setup(
    name = 'manga-scrapper',
    packages = ['manga-scrapper'],
    version = "0.1",
    description = 'Manga-scrapper is a small image scrapper based on BeautifulSoup4 and cfscrape',
    author = "Daniel Montivero, Nils Gillmann (ng0)",
    author_email = "danielelnuevo@hotmail.com, ng0@n0.is",
    url = "https://c.n0.is/gillmann/manga-scrapper",
    keywords = "manga scraping",
    classifiers = ['Development Status :: 3 - Alpha'],
    platforms = ['Linux'],
    include_package_data = True,
    install_requires = ['cfscrape', 'BeautifulSoup']
)
