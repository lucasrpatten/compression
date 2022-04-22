import os
compile import *
from word_list import word_list as word_list
import collections
from operator import itemgetter


def phase1(file_string, data_file="data.txt"):
    data_file = open(data_file, "w")
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
    data_file.write(shorter + file_string)
    os.system('cls' if os.name=='nt' else 'clear')
    print("phase 1:\n 100% complete")
    data_file.close()

def phase2(string):
    c = collections.Counter(string[i:] for i in range(len(string)))
    print(f"{c}")

    # lengths = []
    # for d in range(lower_value, upper_value + 1):
    #     list = []
    #     K = d
    #     list.append([string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if len(string[i:j]) == K])
    #     for b in list:
    #         if list.count(b) < 4:
    #             list.remove(b)
    #     lengths.append(list)
    # return lengths
