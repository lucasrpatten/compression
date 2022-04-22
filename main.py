from compile import *
import os#, nltk
import phases



def main():
    file_string = read_file('enwik7')
# Phase 1
    phases.phase1(file_string)
# Phase 2
    print(phases.phase2(file_string))

    data_file = open('data.txt', 'r');dataset = data_file.read();data_file.close()
    write_lzma(dataset)
    print('done')
main()

# x = open('enwik8', 'r');write_lzma(x.read());x.close()
