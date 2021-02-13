import operator
import os
from json import dump, load


def analyize_text():

    input_file = open('tokenized_text.json')
    output_file = open('word_map.json', 'w')
    articles = load(input_file)

    most_common_words_map = []

    for article in articles:

        words_map = {}

        for word in article['title']:
            if words_map.get(word):
                words_map[word] += 3
            else:
                words_map[word] = 3

        for word in article['article']:
            if words_map.get(word):
                words_map[word] += 3
            else:
                words_map[word] = 3

        words_map = sorted(
            words_map.items(), key=operator.itemgetter(1))[-5:]

        most_common_words_map.append({
            article['id']: words_map
        })

    dump(most_common_words_map, output_file, ensure_ascii=False)
    os.remove('tokenized_text.json')


if __name__ == '__main__':
    analyize_text()
