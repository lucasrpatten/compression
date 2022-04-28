def decomp_phase1(file):
    with open(file, 'r') as f:
        file_compressed = f.read()
        file = file_compressed.split('\n#p1\n')
        word_dict = file[0].split('\n')
        uncompressed_string = file[1]
        for i in range(len(word_dict)-1):
            pair = word_dict[i].split(':')
            uncompressed_string = uncompressed_string.replace(pair[0], pair[1])
        f.close()
        return uncompressed_string
opened = open('unarchived', 'w')
opened.write(decomp_phase1('data.txt'))
opened.close()
