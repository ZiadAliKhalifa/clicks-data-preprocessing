import csv
import os
from json import dump
from arabicstopwords.arabicstopwords import is_stop


def tokenize_text():

    output_file = open('tokenized_text.json', 'w')

    with open('clean_news_articles.csv',  "rt", encoding="utf-8") as csvfile:
        datareader = csv.reader(csvfile)

        tokenized_articles = []

        for row in datareader:
            splitted_title = str.split(row[1], " ")
            splitted_article = str.split(row[2], " ")

            stripped_title = [
                word for word in splitted_title if not is_stop(word) and not str.isspace(word)]
            stripped_article = [
                word for word in splitted_article if not is_stop(word) and not str.isspace(word)]

            tokenized_articles.append({
                'id': row[0],
                'title': stripped_title,
                'article': stripped_article
            })

        dump(tokenized_articles, output_file, ensure_ascii=False)

    # Remove the previous CSV file that was used as input
    os.remove('clean_news_articles.csv')


if __name__ == '__main__':
    tokenize_text()
