# -* coding:utf-8 *-
__author__ = 'nancy'


def readfile(path1, size=100):
    size = size * 1024 * 1024

    with open(path1, 'r') as f:
        while True:
            read1 = f.read(size)
            if read1:
                yield read1
            else:
                break

if __name__ == "__main__":
    path = '/Users/nancy/Downloads/test.xml'
    i = 0
    for piece in readfile(path, 1):
        i += 1
    print(i)
