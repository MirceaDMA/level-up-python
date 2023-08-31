import string

def is_palindrome(phrase):
    formatted_phrase = phrase.lower()
    for char in string.punctuation:
        formatted_phrase = formatted_phrase.replace(char, "")
    formatted_phrase = formatted_phrase.replace(" ", "")
    reverse_phrase = formatted_phrase[::-1]
    return formatted_phrase == reverse_phrase


is_palindrome("He lived as a devil, eh?")
