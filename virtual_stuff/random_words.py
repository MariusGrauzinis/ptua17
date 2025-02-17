from random_word import RandomWords

r = RandomWords()
words = [r.get_random_word() for _ in range(5)]

for word in sorted(words):
    print(word.upper())