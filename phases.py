import os
from compile import *
from word_list import word_list as word_list
import collections
from operator import itemgetter
import regex as re
import time
def phase1(file_string, data_file="data.txt"):
    start = time.time()
    data_file = open(data_file, "w")
    shorter = ""
    for i in range(len(word_list)):
        current_word = word_list[i]
        occurences = file_string.count(current_word)
        if occurences > len(current_word)+6:
            os.system('cls' if os.name=='nt' else 'clear')
            print(f"phase 1:\n{i/220000*100:.2f} % complete\telapsed time: {time.time() - start}")
            key = random_string()
            key = check_key(key, file_string)
            shorter += f"{key}:{current_word}\n"
            file_string = file_string.replace(current_word, key)
    data_file.write(shorter + file_string)
    os.system('cls' if os.name=='nt' else 'clear')
    print("phase 1:\n 100% complete")
    data_file.close()
 
def phase2(string, lower_range=1, upper_range=10):
    print("phase 2: Starting")
    values = {}
    for n in range(lower_range, upper_range):
        os.system('cls' if os.name=='nt' else 'clear')
        print(f'{n} - Current iteration\n– - Phase 2\n{upper_range} - Total iterations')
        string_list = string[::n]
        inarow = 0
        current_char = ""
        current_values = []
        for i in range(len(string_list)): 
            if string_list[i] == current_char:
                inarow += 1
            elif inarow >= len(str(i))+len(str(i))+len(str(n))+15:
                inarow += 1
                if string_list[i-1] != '.':
                    current_values.append(f"{n}.{i-inarow}.{inarow}.{string_list[i]}")
                    current_char = str(string_list[i])
                else:
                    current_values.append(f"{n}.{i-inarow}.{inarow}.period")
                    current_char = str(string_list[i])
                inarow = 0
            else:
                current_char = str(string_list[i])
                inarow = 0
        try:
            current_values[0]
            values[n] = current_values
        except IndexError:
            pass
        pattern_list = []
        for e in range(len(current_values)):
            pattern_list.append(current_values[e])
        pattern_list = patComp.sort(pattern_list)
        new_value = ""
        last_upper = 0
        for q in range(len(pattern_list)):
            stripped_string = str(string[int(patNot.location(pattern_list[q])):(int(patNot.location(pattern_list[q]))+int(patNot.inarow(pattern_list[q])))].strip([::9]))
            if int(patNot.location(pattern_list[q])) != last_upper:
                new_value = new_value + string[last_upper:int(patNot.location(pattern_list[q])]
                new_value = new_value + stripped_string
                last_upper = int(patNot.location(pattern_list[q]) + patNot.inarow(pattern_list[q]))
            else:
                new_value = new_value + stripped_string
                last_upper = int(patNot.location(pattern_list[q]) + patNot.inarow(pattern_list[q]))

            #active_value = current_values[e]
            #value, location, amount, item = patNot.value(active_value), patNot.location(active_value), patNot.inarow(active_value), patNot.item(active_value)
    return values, string


    #c = collections.Counter(string[i:] for i in range(len(string)))
    #print(f"{c}")

    # lengths = []
    # for d in range(lower_value, upper_value + 1):
    #     list = []
    #     K = d
    #     list.append([string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if len(string[i:j]) == K])
    #     for b in list:
    #         if list.count(b) < 4:
    #             list.remove(b)
    #     lengths.append(list)
#     # return lengths
