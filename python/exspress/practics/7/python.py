count_words = {}
with open('moby_01_clean.txt') as infile:
    for line in infile:
        for word in line.split():
            count_words[word] = count_words.get(word, 0) + 1
word_value = list(count_words.values())
max_word_keys = []
min_word_keys = []
for count_word in count_words:
    if count_words[count_word] == max(word_value):
        max_word_keys.append(count_word)
    if count_words[count_word] == min(word_value):
        min_word_keys.append(count_word)
print("\tСамые частые слова {0}; \n\tСамые редкие слова {1} \n".format(max_word_keys, min_word_keys))
