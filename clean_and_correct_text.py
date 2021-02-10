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

    for row in datareader:
        # Remove punctuation from the title and the article
        cleaned_title = text_cleaner.remove_punctuations(row[1])
        cleaned_article = text_cleaner.remove_punctuations(row[2])

        # Correct spelling

        # Split titles and articles into words
        # Check if any of the words are in the common mistakes dict
        # Replace them with correct value if they do
        splitted_title = str.split(cleaned_title, " ")
        splitted_article = str.split(cleaned_article, " ")

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

        corrected_title = ' '.join(corrected_title_array)
        corrected_article = ' '.join(corrected_article_array)

        # Write it output to a new CSV file
        writer.writerow([row[0], corrected_title, corrected_article])

# Remove the previous CSV file that was used as input
os.remove('news_articles.csv')
