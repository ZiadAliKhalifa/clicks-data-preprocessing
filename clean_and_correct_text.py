import os
import csv
from json import load

from Utils.text_cleaner import CleanText

dictionary_file = open('../Resources/word_dictionary.json')
dictionary = load(dictionary_file)


output_file = open('no_punc_news_articles.csv', 'w')
writer = csv.writer(output_file)
text_cleaner = CleanText()

with open('news_articles.csv',  "rt", encoding="utf-8") as csvfile:
    datareader = csv.reader(csvfile)

    count = 0

    for row in datareader:

        count += 1
        # Remove punctuation from the title and the article
        cleaned_title = text_cleaner.remove_punctuations(row[1])
        cleaned_article = text_cleaner.remove_punctuations(row[2])

        # Correct spelling
        splitted_title = str.split(cleaned_title, " ")
        splitted_article = str.split(cleaned_article, " ")

        print("+++++++++++")
        print(row[0])
        print(len(splitted_article))

        corrected_title_array = []
        corrected_article_array = []

        for word in splitted_title:
            if dictionary.get(word):
                corrected_title_array.append(dictionary.get(word))
            else:
                corrected_title_array.append(word)

        for word in splitted_article:
            if dictionary.get(word):
                corrected_article_array.append(dictionary.get(word))
            else:
                corrected_article_array.append(word)

        print(len(corrected_article_array))

        corrected_title = ' '.join(corrected_title_array)
        corrected_article = ' '.join(corrected_article_array)

        print(len(corrected_article))
        print("-------------")

        writer.writerow([row[0], corrected_title, corrected_article])

os.remove('news_articles.csv')
