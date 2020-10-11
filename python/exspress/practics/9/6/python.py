import string


def delete_punctuations(parameter):
    delete_list = list(string.punctuation)
    word_line = list(parameter)
    for delete_char in delete_list:
        while word_line.count(delete_char):
            word_line.remove(delete_char)
    return "".join(word_line)


with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        line = line.lower()
        line = line.rstrip('/n')
        line = line.strip()
        line = delete_punctuations(line)
        clean_words = line.split(" ")
        for clean_word in clean_words:
            outfile.write(clean_word+' ')
