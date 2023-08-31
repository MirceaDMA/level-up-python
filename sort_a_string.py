# sort words alpabetically: solution 1
def sort_words_1(words_to_sort):
    words = [word.lower()+word for word in words_to_sort.split()]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    print(' '.join(words))
    return ' '.join(words)

# sort words alpabetically: solution 2
def sort_words_2(words_to_sort):
    return " ".join(sorted(words_to_sort.split(), key=str.casefold))
