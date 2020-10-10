import string

delete_list = list(string.punctuation)

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        line = line.lower()
        line = line.rstrip('/n')
        word_line = list(line)
        for delete_char in delete_list:
            while word_line.count(delete_char):
                word_line.remove(delete_char)
        line = "".join(word_line)
        line = line.strip()
        clean_words = line.split(" ")
        for clean_word in clean_words:
            outfile.write(clean_word+' ')
