import string

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        line = line.lower()
        punt_list = list(string.punctuation)
        word_line = list(line)
        for punt in punt_list:
            for i in range(word_line.count(punt)):
                word_line.remove(punt)
        line = "".join(word_line)
        line = line.strip()
        clean_words = line.split(" ")
        for clean_word in clean_words:
            outfile.write(clean_word+'\n')
