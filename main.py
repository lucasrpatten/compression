from compile import *
import os#, nltk
import phases

def main():
    file_string = read_file('enwik8')
# Phase 1
    #phases.phase1(file_string)
# Phase 2
    print(phases.phase2(file_string))

    data_file = open('data.txt', 'r');dataset = data_file.read();data_file.close()
    write_lzma(dataset)
    original_size = os.popen('ls -l enwik8').read()
    compressed_size = os.popen('ls -l compressed').read()
    print(f"Original: {original_size}\nCompressed: {compressed_size}")
main()

# x = open('enwik8', 'r');write_lzma(x.read());x.close()
