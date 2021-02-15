import pytest
import requests
from rabota_by_parser.rabota_by_parser import AverageNumbers, Parser


class TestParser:

    def setup(self):
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.url = [requests.get("https://rabota.by/vacancy/41683035?query=python", headers=self.headers),
                    requests.get("https://rabota.by/vacancy/40520308?query=python", headers=self.headers)]
        self.word = ["shotgun"]

    def test_find_shotgun(self):
        shotgun = Parser(self.word, self.url).page_with_vacancy()
        assert sum(shotgun["shotgun"]) == 0


@pytest.mark.parametrize('all_words, result', [
    ({'python': [1, 2, 3, 4, 5]}, {'python': [3]}),
    ({'flask': []}, {'flask': [0]}),
    ({'linux': [0, 0, 0]}, {'linux': [0]})
])
def test_average_numbers(all_words, result):
    assert AverageNumbers(all_words).average_number() == result
