import pytest
import requests
from bs4 import BeautifulSoup
from rabota_by_parser.generate_urls import GetPages, GenerateLinksCV


class TestGetPages:

    @pytest.fixture()
    def setup(self):
        self.url = 'https://rabota.by/search/vacancy?area=16&fromSearchLine=true&st=searchVacancy&text=python'
        self.links = []
        self.generate_page = GetPages(self.url)

    def test_get_pages(self, setup):
        assert len(self.generate_page.generate_pages()) == 9


class TestGenerateLinksCV:

    def setup(self):
        self.url = 'https://rabota.by/search/vacancy?area=16&fromSearchLine=true&st=searchVacancy&text=python'
        self.generate = GenerateLinksCV(self.url)
        self.headers = {'user-agent': 'my-app/0.0.1'}

    @pytest.mark.skip(reqson="Because it's too long")
    def test_count_links(self):
        assert len(self.generate.generate_links()) == 50
