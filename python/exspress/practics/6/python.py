import string

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        line = line.lower()
        punct_list = list(string.punctuation)
        word_line = list(line)
        for punct in punct_list:
            for i in range(word_line.count(punct)):
                word_line.remove(punct)
        line = "".join(word_line)
        line = line.strip()
        clean_words = line.split(" ")
        print(clean_words)
        for clean_word in clean_words:
            outfile.write(clean_word+'\n')
