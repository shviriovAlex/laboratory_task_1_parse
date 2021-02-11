import requests
from bs4 import BeautifulSoup
import re


class Urls:
    def __init__(self, main_url):
        self.main_url = main_url
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.count_page = 0
        self.all_urls = []

    def correct_url(self):
        try:
            r = requests.get(self.main_url, headers=self.headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print('Incorrect URL', err)

    def count_pages(self):
        page_number = BeautifulSoup(requests.get(self.main_url, headers=self.headers).content,
                                    "html.parser").find_all(class_="bloko-button HH-Pager-Control")
        for page in page_number:
            self.count_page = int(page["data-page"]) + 1

        for page in range(self.count_page):
            self.main_url = self.main_url[:-1]
            self.main_url += str(page)
            self.all_urls.append(self.main_url)

        return self.all_urls


class Parser:

    def __init__(self, words):
        self.words = words
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.all_words = {'python': [], 'flask': [], 'linux': []}

    def page_with_vacancy(self):
        for url in urls.count_pages():
            for cv_link in BeautifulSoup(requests.get(url, headers=self.headers).content, 'html.parser').find_all(
                    class_="bloko-link HH-LinkModifier"):
                cv_page = requests.get(cv_link['href'], headers=self.headers)
                cv_page_soup = BeautifulSoup(cv_page.content, 'html.parser').find_all(
                    class_="bloko-gap bloko-gap_bottom")

                [self.all_words[word].append(len(re.findall(word, str(cv_page_soup).lower()))) for word in self.words]

        return f"Аmount word Python{self.all_words['python']}\n" \
               f"Аmount word Flask{self.all_words['flask']}\n" \
               f"Аmount word Linux{self.all_words['linux']}"

    def average_number(self):
        return f"Average number Python {sum(self.all_words['python']) / len(self.all_words['python'])}\n" \
               f"Average number Flask, {sum(self.all_words['flask']) / len(self.all_words['flask'])}\n" \
               f"Average number Linux, {sum(self.all_words['linux']) / len(self.all_words['linux'])}"


if __name__ == '__main__':
    urls = Urls('https://rabota.by/search/vacancy?L_is_autosearch=false&area=16&clusters=true&enable_snippets=true&text=Python&page=0')
    pars = Parser(['python', 'flask', 'linux'])
    urls.correct_url()
    urls.count_pages()
    print(pars.page_with_vacancy())
    print(pars.average_number())

