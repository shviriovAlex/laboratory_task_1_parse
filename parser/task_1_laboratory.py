import requests
from requests import exceptions
from bs4 import BeautifulSoup
import re


class CorrectUrl:
    def __init__(self, url):
        self.url = url
        self.headers = {'user-agent': 'my-app/0.0.1'}

    def check_url(self):
        try:
            r = requests.get(self.url, headers=self.headers)
            r.raise_for_status()
            print('Successful connection!')
        except exceptions.HTTPError:
            print('Something went wrong.Incorrect URL or check your internet connection!')
            quit('Check if the address is correct')
        except exceptions.ConnectionError:
            print(f"Something went wrong. Server Error!\nCan't find {self.url}!")
            quit('Check if the address is correct')
        except exceptions.MissingSchema:
            print(f"Something went wrong. Invalid url!\nTry https://{self.url}!")
            quit('Check if the address is correct')
        except exceptions.InvalidSchema:
            print(f"Something went wrong. Invalid url {self.url}!")
            quit('Check if the address is correct')


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

        for page in range(self.count_pages):
            self.main_url += str(page)
            CorrectUrl(self.main_url).check_url()
            self.all_urls.append(self.main_url)
            self.main_url = self.main_url[:-len(str(page))]

        return self.all_urls


class Parser:

    def __init__(self, words, all_urls):
        self.words = words
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.all_words = {'python': [], 'flask': [], 'linux': []}
        self.links = []
        self.all_urls = all_urls

    def page_with_vacancy(self):
        for url in self.all_urls:
            for cv_link in BeautifulSoup(requests.get(url, headers=self.headers).content, 'html.parser').find_all(
                    class_="bloko-link HH-LinkModifier"):
                cv_page = requests.get(cv_link['href'], headers=self.headers)
                self.links.append(cv_page)
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


a = GetPages(
    f"https://rabota.by/search/vacancy?L_is_autosearch=false&area=16&clusters=true&enable_snippets=true&text=python&page=")
print(a.generate_pages())
b = Parser(['python', 'flask', 'linux'], a)

print(b.page_with_vacancy())

