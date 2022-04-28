import string

alphanum = string.ascii_lowercase + string.digits + string.ascii_uppercase

combs = [val1+val2 for val1 in alphanum for val2 in alphanum]
enwik8 = open('enwik8', 'r')
file_string = enwik8.read()
enwik8.close()
notin = []
for i in range(len(combs)):
    if str(combs[i]) not in file_string:
        notin.append(str(combs[i]))
    else:
        continue
with open("notinbut2.py", "w") as file:
    file.write(f'listoflength2 = {notin}')
    file.close()
    
