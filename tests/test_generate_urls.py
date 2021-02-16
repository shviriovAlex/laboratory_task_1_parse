import pytest
from rabota_by_parser.generate_urls import GetPages, GenerateLinksCV


class TestGetPages:

    def test_get_pages(self, main_url):
        assert len(GetPages(main_url).generate_pages()) == 9


class TestGenerateLinksCV:

    @pytest.mark.skip(reason="Because it's too long")
    def test_count_links(self, main_url):
        assert len(GenerateLinksCV(main_url).generate_links()) == 50
