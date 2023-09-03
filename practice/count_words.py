import re
import collections

def count_words(path):
    with open(path, "r", encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]

        print(f"Total number of words: {len(all_words)}")

        counter = collections.Counter(all_words)
        common_words = counter.most_common(20)
        for word in common_words:
          print(f"{word[0]} \t{word[1]}")

if __name__ == "__main__":
   count_words("./practice/files/pg100.txt")