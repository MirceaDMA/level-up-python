def sort_words(words_to_sort):
    words = [word.lower()+word for word in words_to_sort.split()]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    print(''.join(words))
    return ' '.join(words)
