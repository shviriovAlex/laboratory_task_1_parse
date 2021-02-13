from bs4 import BeautifulSoup
import re


class Parser:

    def __init__(self, words, all_urls):
        self.words = words
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.all_words = {}
        self.all_urls = all_urls

    def page_with_vacancy(self):
        for cv_page in self.all_urls:
            cv_page_soup = BeautifulSoup(cv_page.content, 'html.parser').find_all(
                class_="bloko-gap bloko-gap_bottom")
            for word in self.words:
                if word not in self.all_words:
                    self.all_words.setdefault(word, [len(re.findall(word, str(cv_page_soup).lower()))])
                else:
                    self.all_words[word].append(len(re.findall(word, str(cv_page_soup).lower())))
            # [self.all_words.setdefault(word, [len(re.findall(word, str(cv_page_soup).lower()))]) if word not in self.all_words else self.all_words[word].append(len(re.findall(word, str(cv_page_soup).lower()))) for word in self.words]
        return self.all_words


class AverageNumbers:

    def __init__(self, all_words):
        self.all_words = all_words
        self.average_number_words = {}

    def average_number(self):
        for word in self.all_words:
            self.average_number_words.setdefault(word, [sum(self.all_words[word]) / len(self.all_words[word])])
        return self.average_number_words
