import unittest
from main import remove_duplicates, concat_strings, get_longest_word, count_vowels

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_basic(self):
        result = remove_duplicates("hello")
        self.assertEqual(result, "helo")

    def test_remove_duplicates_empty_str(self):
        result = remove_duplicates("")
        self.assertEqual(result, "")

    def test_remove_duplicates_none_str(self):
        result = remove_duplicates("hiiiii")
        self.assertEqual(result, "hi")

    def test_remove_duplicates_special_chars(self):
        result = remove_duplicates("!@#hello$%^")
        self.assertEqual(result, "!@#helo$%^")

class TestConcatStrings(unittest.TestCase):

    def test_concat_strings_basic(self):
        result = concat_strings("hello", "world")
        self.assertEqual(result, "helloworld")

    def test_concat_strings_empty_str(self):
        result = concat_strings("", "world")
        self.assertEqual(result, "world")

    def test_concat_strings_none_str(self):
        result = concat_strings("", "Hiworld")
        self.assertEqual(result, "Hiworld")

    def test_concat_strings_ints(self):
        result = concat_strings("hello", str(123))
        self.assertEqual(result, "hello123")

class TestCountVowels(unittest.TestCase):

    def test_count_vowels(self):
        word = "Hello"
        self.assertEqual(count_vowels(word), 2)

    def test_count_vowels_empty_string(self):
        word = ""
        self.assertEqual(count_vowels(word), 0)

    def test_count_vowels_no_vowels(self):
        word = "xyz"
        self.assertEqual(count_vowels(word), 0)

    def test_count_vowels_all_vowels(self):
        word = "AEIOUaeiou"
        self.assertEqual(count_vowels(word), 10)

class TestGetLongestWord(unittest.TestCase):

    def test_get_longest_word(self):
        sentence = "The quick brown fox jumpss over the lazy dog"
        self.assertEqual(get_longest_word(sentence), "jumpss")

    def test_get_longest_word_empty_string(self):
        sentence = "this is a test softwareeng"
        self.assertEqual(get_longest_word(sentence), "softwareeng")

    def test_get_longest_word_single_word(self):
        sentence = "test"
        self.assertEqual(get_longest_word(sentence), "test")

    def test_get_longest_word_multiple_longest_words(self):
        sentence = "The quick brown fox jumpsss over the lazy dog jumps over the fence"
        self.assertEqual(get_longest_word(sentence), "jumpsss")


if __name__ == '__main__':
    unittest.main()
