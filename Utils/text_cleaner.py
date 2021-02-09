import string
import re


class CleanText():

    _arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
    _english_punctuations = string.punctuation
    _punctuations_list = _arabic_punctuations + _english_punctuations

    _arabic_diacritics = re.compile("""
                                ّ    | # Tashdid
                                َ    | # Fatha
                                ً    | # Tanwin Fath
                                ُ    | # Damma
                                ٌ    | # Tanwin Damm
                                ِ    | # Kasra
                                ٍ    | # Tanwin Kasr
                                ْ    | # Sukun
                                ـ     # Tatwil/Kashida
                            """, re.VERBOSE)

    def normalize_arabic(self, text):
        text = re.sub("[إأآا]", "ا", text)
        text = re.sub("ى", "ي", text)
        text = re.sub("ؤ", "ء", text)
        text = re.sub("ئ", "ء", text)
        text = re.sub("ة", "ه", text)
        text = re.sub("گ", "ك", text)
        return text

    def remove_diacritics(self, text):
        text = re.sub(self._arabic_diacritics, '', text)
        return text

    def remove_punctuations(self, text):
        translator = str.maketrans('', '', self._punctuations_list)
        return text.translate(translator)

    def remove_repeating_char(self, text):
        return re.sub(r'(.)\1+', r'\1', text)
