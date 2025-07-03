def to_upper(s):
    return s.upper()


def to_lower(s):
    return s.lower()


def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())


def reverse_string(s):
    return s[::-1]


def strip_spaces(s):
    return s.strip()


def is_palindrome(s):
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]


def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")


def count_consonants(s):
    return sum(1 for char in s.lower() if char.isalpha() and char not in "aeiou")


def remove_punctuation(s):
    import string
    return ''.join(char for char in s if char not in string.punctuation)


def get_unique_words(s):
    return set(s.split())


def word_frequencies(s):
    words = s.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def repeat_string(s, times):
    return s * times


def truncate_string(s, length):
    return s[:length] + '...' if len(s) > length else s


def title_case(s):
    return s.title()
