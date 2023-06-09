def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

def concat_strings(s1, s2):
    return s1 + s2

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def get_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
