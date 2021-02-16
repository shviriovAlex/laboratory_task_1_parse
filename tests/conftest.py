import pytest


@pytest.fixture
def headers():
    return {'user-agent': 'my-app/0.0.1'}


@pytest.fixture
def main_url():
    return "https://rabota.by/search/vacancy?L_is_autosearch=false&area=16&clusters=true&enable_snippets=true&text=python&page="



