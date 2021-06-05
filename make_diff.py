'''
make diff file
'''
with open('f1.txt', 'r') as file1, open('f2.txt', 'r') as file2,  open('diff.txt', 'a') as diff:
    f2 = file2.read()
    for line in file1:
        if line not in f2:
            diff.write(line)
# with open('diff.txt', 'r') as d:
print(open('diff.txt', 'r').read())
