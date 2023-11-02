import pytest
import requests
from rabota_by_parser.rabota_by_parser import AverageNumbers, Parser
from rabota_by_parser.generate_urls import GenerateLinksCV


@pytest.mark.parametrize('word, url', [
    (['shotgun'], ["https://rabota.by/vacancy/41683035?query=python"]),
    (['shotgun'], ["https://rabota.by/vacancy/40520308?query=python"])
])
def test_find_shotgun(word, url, headers):
    url = [requests.get(url[0], headers=headers)]
    shotgun = Parser(word, url).page_with_vacancy()
    assert sum(shotgun["shotgun"]) == 0


@pytest.mark.parametrize('all_words, result', [
    ({'python': [1, 2, 3, 4, 5]}, {'python': [3]}),
    ({'flask': []}, {'flask': [0]}),
    ({'linux': [0, 0, 0]}, {'linux': [0]})
])
def test_average_numbers(all_words, result):
    assert AverageNumbers(all_words).average_number() == result


@pytest.mark.parametrize('url, words', [
    (["https://rabota.by/vacancy/41683035?query=python"], ['python']),
    (["https://rabota.by/vacancy/40520308?query=python"], ['flask']),
    (["https://rabota.by/vacancy/41595848?query=python"], ['linux'])
])
def test_around_number(url, words, headers):
    url = [requests.get(url[1], headers=headers)]
    dict_words = Parser(words, url).page_with_vacancy()
    assert 0.5 <= AverageNumbers(dict_words).average_number()[words[0]][0] <= 1.5


@pytest.mark.parametrize('url, words', [
    (["https://rabota.by/vacancy/41683035?query=python"], ['python']),
    (["https://rabota.by/vacancy/40520308?query=python"], ['flask']),
    (["https://rabota.by/vacancy/41595848?query=python"], ['linux'])
])
def test_around_number_2(url, words, headers):
    url = [requests.get(url[1], headers=headers)]
    dict_words = Parser(words, url).page_with_vacancy()
    assert 0.5 <= AverageNumbers(dict_words).average_number()[words[0]][0] <= 1.5


@pytest.mark.parametrize('url, words', [
    (["https://rabota.by/vacancy/41683035?query=python"], ['python']),
    (["https://rabota.by/vacancy/40520308?query=python"], ['flask']),
    (["https://rabota.by/vacancy/41595848?query=python"], ['linux'])
])
def test_around_number_3(url, words, headers):
    url = [requests.get(url[1], headers=headers)]
    dict_words = Parser(words, url).page_with_vacancy()
    assert 0.5 <= AverageNumbers(dict_words).average_number()[words[0]][0] <= 1.5


@pytest.mark.parametrize('url, words', [
    (["https://rabota.by/vacancy/41683035?query=python"], ['python']),
    (["https://rabota.by/vacancy/40520308?query=python"], ['flask']),
    (["https://rabota.by/vacancy/41595848?query=python"], ['linux'])
])
def test_around_number_2(url, words, headers):
    url = [requests.get(url[1], headers=headers)]
    dict_words = Parser(words, url).page_with_vacancy()
    assert 0.5 <= AverageNumbers(dict_words).average_number()[words[0]][0] <= 1.5


@pytest.mark.parametrize('url, words', [
    (["https://rabota.by/vacancy/41683035?query=python"], ['python']),
    (["https://rabota.by/vacancy/40520308?query=python"], ['flask']),
    (["https://rabota.by/vacancy/41595848?query=python"], ['linux'])
])
def test_around_number_3(url, words, headers):
    url = [requests.get(url[1], headers=headers)]
    dict_words = Parser(words, url).page_with_vacancy()
    assert 0.5 <= AverageNumbers(dict_words).average_number()[words[0]][0] <= 1.5