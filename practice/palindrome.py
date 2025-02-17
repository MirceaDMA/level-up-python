# my method using string module
import string

def is_palindrome(phrase):
    formatted_phrase = phrase.lower()
    for char in string.punctuation:
        formatted_phrase = formatted_phrase.replace(char, "")
    formatted_phrase = formatted_phrase.replace(" ", "")
    reverse_phrase = formatted_phrase[::-1]
    return formatted_phrase == reverse_phrase

# second method using ReGex
import re

def is_it_palindrome(phrase):
    formatted_phrase = "".join(re.findall(r"[a-z]+", phrase.lower()))
    reversed_phrase = formatted_phrase[::-1]
    return formatted_phrase == reversed_phrase
