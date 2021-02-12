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

    def normalize_arabic_alphabet(self, text):
        """
            Replace any special characters for unity
        """
        text = re.sub("[إأآا]", "ا", text)
        text = re.sub("ى", "ي", text)
        text = re.sub("ؤ", "ء", text)
        text = re.sub("ئ", "ء", text)
        text = re.sub("ة", "ه", text)
        text = re.sub("گ", "ك", text)
        return text

    def remove_diacritics(self, text):
        """
            Remove all diacritic symbols
        """
        text = re.sub(self._arabic_diacritics, '', text)
        return text

    def remove_punctuations(self, text):
        """
            Remove all punctuation symbols
        """
        translator = str.maketrans('', '', self._punctuations_list)
        return text.translate(translator)

    def remove_repeating_char(self, text):
        """
            Remove all repeating characters
        """
        return re.sub(r'(.)\2+', r'\1', text)

    def normalize_text(self, text):
        """
            Runs all methods of class on a string of text
        """
        text = self.normalize_arabic_alphabet(text)
        text = self.remove_diacritics(text)

        return text
