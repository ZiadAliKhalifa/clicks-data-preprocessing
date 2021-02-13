from xml2csv import parse_xml_articles
from clean_and_correct_text import clean_and_correct_text
from tokenize_text import tokenize_text
from analyze_text import analyize_text


def main():
    parse_xml_articles()
    clean_and_correct_text()
    tokenize_text()
    analyize_text()


if __name__ == '__main__':
    main()
