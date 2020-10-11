def count_word(string):
    for word in string.split():
        count_words[word] = count_words.get(word, 0) + 1
    return count_words


def max_word(words):
    max_word_keys = []
    word_value = list(words.values())
    for word in words:
        if words[word] == max(word_value):
            max_word_keys.append(word)
    return " ".join(max_word_keys)


def min_word(words):
    min_word_keys = []
    word_value = list(words.values())
    for word in words:
        if words[word] == min(word_value):
            min_word_keys.append(word)
    return " ".join(min_word_keys)


count_words = {}

with open('moby_01_clean.txt') as infile:
    for line in infile:
        count_words = count_word(line)
print("\tСамые частые слова {0}; \n\tСамые редкие слова {1} \n".format(max_word(count_words), min_word(count_words)))
