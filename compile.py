from dahuffman import HuffmanCodec 
from scipy.interpolate import lagrange
import random, lzma
import string as st
import regex as re
def generate_pList(object):
    object = object.split('.')
    if object[-1] == 'period':
        object[-1] = '.'
    else:
        pass
    return object
class patternNotation: # format - ,what_split.where.how_many.what., - ex 2.1435.133. . representing every other pattern, at index 1435, 133 in a row of space
    #I will probably make a github exclusively for pattern detection and pattern data types later - just so ya'll know
    def __init__(self, patternObject):
        self.pList = generate_pList(patternObject)
        self.patternObject = patternObject
        self.pObj = self.patternObject # short for patternObject
        self.value_ = self.pList[0]
        self.location = selfPlist[1]
        self.inarow = selfPlist[2]
        self.item = selfPlist[3]

class patNot(patternNotation):#short for pattern notation
    pass


class patComp:
    def __init__(self, patternTable):
        self.length = len(patternTable)
        self.table = patternTable
    def sort(self):
        sortDict = {}
        for i in (0, self.length):
            print(self.length)
            sortDict[int(patternNotation.value_(self.table[i]))] = self.table[i]
        sorted = dict(sorted(sortDict.items()))
        return list(sorted)

class patternCompare(patComp):
    pass

def read_file(file_name = 'enwik9'):
    file = open(file_name, 'r')
    file_string = file.read()
    return file_string

def split_file(file ,splitter=" "):
    return file.split(splitter)
def huffman(string):
    codec = HuffmanCodec.from_data(string)
    return codec.encode(string)
def find_poly(x, y):
    return lagrange(x, y)
def write_lzma(to_compress):
    file = lzma.LZMAFile('compressed', mode='w', preset=9)
    file.write(bytes(str(to_compress).encode('utf-8')))
    file.close()
    return None
def random_string(length=5):
    return ''.join(random.SystemRandom().choice(st.ascii_letters + st.digits) for _ in range(length))
def in_data(string, data):
    if string in data:
        return True
    else:
        return False
def check_key(string, data, string_length=5):
    while in_data(string, data) == True:
        string = random_string(string_length)
    return string

def split_string(string, lower, upper, n):
    return [string[i:i+n] for i in range(lower, upper, n)]

def into_dict(file_string):
    file_table = split_file(file_string)
    items = {}
    current_value = 0
    for i in range(len(file_table)):
        keys = items.keys()
        if file_table[i] not in keys:
            items[file_table[i]] = i
        elif file_table[i] in keys:
            key = items[file_table[i]]
            key = f"{key} {i}"
            items[file_table[i]] = key
        else:
            print('\n\n\nERROR')
            break
    return items
def all_string(length=3):
    return list(map(''.join, product(st.printable.split(""), repeat=length)))
