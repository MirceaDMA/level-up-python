import secrets

def generate_passphrase(num_words, wordlist_path="./practice/files/diceware.wordlist.asc"):
    with open(wordlist_path, "r", encoding="utf-8") as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]
   
    words = [secrets.choice(word_list) for i in range(num_words)]
    print(words)

if __name__ == "__main__":
    generate_passphrase(5)
