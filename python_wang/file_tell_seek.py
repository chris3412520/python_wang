from uu import decode

with open('test.txt', 'r') as f:
    print(f.tell())
    print(f.read(5),decode('utf-8'))
    print(f.tell())
    print(f.read(5),decode('utf-8'))