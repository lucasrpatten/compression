import nltk
def create_dict(file_name):
    dictionary = open(file_name, 'w')
    nltk.download('words')
    word_list = nltk.corpus.words.words()
    new = []
    for i in word_list:
        if len(i) > 5:
            new.append(i)
    dictionary.write(f"word_list = {new}")
    dictionary.close
create_dict('word_list.py')