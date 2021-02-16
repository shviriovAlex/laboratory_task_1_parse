import pytest
import requests
from requests import exceptions
from rabota_by_parser.url_check import CorrectUrl


@pytest.mark.parametrize('url, status', [
    ('https://www.google.com/', 200),
    ('https://rabota.by', 200),
])
def test_internet_connection(url, status, headers):
    assert requests.head(url, headers=headers).status_code == 200


@pytest.mark.parametrize('url, error', [
    ('https://raa.by', exceptions.ConnectionError),
    ('ht://rabota.by', exceptions.InvalidSchema),
    ('rabota.by', exceptions.MissingSchema)
])
def test_raise_connection_error(url, error):
    with pytest.raises(error):
        assert CorrectUrl(url).check_url() == error
