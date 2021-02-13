import requests
from bs4 import BeautifulSoup
from parser.url_check import CorrectUrl


class GetPages:

    def __init__(self, main_url, count_pages=None):
        self.main_url = main_url
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.all_urls = []
        self.count_pages = count_pages

    def generate_pages(self):
        CorrectUrl(self.main_url).check_url()
        all_pages = BeautifulSoup(requests.get(self.main_url, headers=self.headers).content,
                                  "html.parser").find_all(class_="bloko-button HH-Pager-Control")
        for page in all_pages:
            self.count_pages = int(page["data-page"]) + 1

        for page in range(1):
            self.main_url += str(page)
            CorrectUrl(self.main_url).check_url()
            self.all_urls.append(self.main_url)
            self.main_url = self.main_url[:-len(str(page))]

        return self.all_urls


class GenerateLinksCV:

    def __init__(self, main_url):
        self.main_url = main_url
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.links = []

    def generate_links(self):

        for url in GetPages(self.main_url).generate_pages():
            for cv_link in BeautifulSoup(requests.get(url, headers=self.headers).content, 'html.parser').find_all(
                    class_="bloko-link HH-LinkModifier"):
                CorrectUrl(cv_link['href']).check_url()
                cv_page = requests.get(cv_link['href'], headers=self.headers)
                self.links.append(cv_page)
        return self.links
