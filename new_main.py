from compile import *
import regex as re
from word_list import word_list as word_list
import math, os, collections#, nltk


def main():
    the_list = open('data.txt', 'w')
    file_string = read_file('enwik8')
# Phase 1
    shorter = ""
    for i in range(len(word_list)):
        current_word = word_list[i]
        occurences = file_string.count(current_word)
        if occurences > len(current_word)+6:
            os.system('cls' if os.name=='nt' else 'clear')
            print("phase 1:\n" + str(round(i/220000*100)) + '% complete')
            key = random_string()
            key = check_key(key, file_string)
            shorter += f"{key}:{current_word}\n"
            file_string = file_string.replace(current_word, key)
    the_list.write(shorter + file_string)
    os.system('cls' if os.name=='nt' else 'clear')
    print("phase 1:\n 100% complete")
# Phase 2
    all_strings = []
    for i in range(0,5):
        print(i)
    the_list.close()
    the_list = open('data.txt', 'r');dataset = the_list.read();the_list.close()
    write_lzma(dataset)
    print('done')
main()

# x = open('enwik8', 'r');write_lzma(x.read());x.close()
