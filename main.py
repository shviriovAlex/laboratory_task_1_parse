from parser.generate_urls import GenerateLinksCV
from parser.parser_rabota_by import Parser, AverageNumbers

if __name__ == '__main__':

    all_links = GenerateLinksCV(f"https://rabota.by/search/vacancy?L_is_autosearch=false&area=16&clusters=true&enable_snippets=true&text=python&page=")
    parse_pages = Parser(['python', 'flask', 'linux'], all_links.generate_links())
    dict_numbers_of_words = parse_pages.page_with_vacancy()
    average_numbers = AverageNumbers(dict_numbers_of_words)
    average_count_words = average_numbers.average_number()
    for word in dict_numbers_of_words:
        print(f"Count word {word} -> {dict_numbers_of_words[word]}")

    for word in average_count_words:
        print(f"Average number word {word} -> {average_count_words[word][0]}")
