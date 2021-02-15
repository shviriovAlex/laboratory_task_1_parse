import pytest
from requests import exceptions
from parser.url_check import CorrectUrl

class TestCheckUrl:

    def setup(self):
        self.url = 'https://rabota.by'
        self.url1 = 'https://raa.by'
        self.url2 = 'ht://rabota.by'
        self.url3 = '.'
        self.url4 = 'rabota.by'
        self.check = CorrectUrl

    def test_raise_connection_error(self):
        with pytest.raises(exceptions.ConnectionError):
            self.check(self.url1).check_url()

    def test_raise_invalid_schema_error(self):
        with pytest.raises(exceptions.InvalidSchema):
            self.check(self.url2).check_url()

    def test_raise_missing_schema_error(self):
        with pytest.raises(exceptions.MissingSchema):
            self.check(self.url3).check_url()

