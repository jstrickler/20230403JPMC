from collections import Counter

FILE_PATH = "DATA/words.txt"

with open(FILE_PATH) as words_in:
    letter_count = Counter(word[0] for word in words_in)

print(f"letter_count: {letter_count}")

print(letter_count.most_common(5))

