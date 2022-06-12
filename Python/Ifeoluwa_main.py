def read_file_content(filename): 
    read_file=open(filename,'r')
    return read_file.read()

def count_words():
    text = read_file_content("./story.txt")
    words=text.split()
    word_count = dict()

    for i in words:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1

    return word_count


count_words()