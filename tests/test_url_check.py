import pytest
import requests
from requests import exceptions
from rabota_by_parser.url_check import CorrectUrl


class TestCheckUrl:

    def setup(self):
        self.headers = {'user-agent': 'my-app/0.0.1'}

    def test_internet_connection(self):
        check_connection = requests.head('https://www.google.com/').status_code
        assert check_connection == 200

    def test_response_200(self):
        status = requests.head('https://rabota.by', headers=self.headers).status_code
        assert status == 200


@pytest.mark.parametrize('url, error', [
    ('https://raa.by', exceptions.ConnectionError),
    ('ht://rabota.by', exceptions.InvalidSchema),
    ('rabota.by', exceptions.MissingSchema)
])
def test_raise_connection_error(url, error):
    with pytest.raises(error):
        assert CorrectUrl(url).check_url() == error
