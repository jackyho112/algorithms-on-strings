# python3
import sys

def BWT(text):
    table = [text[i:] + text[:i] for i in range(len(text))]
    table_sorted = table[:]
    table_sorted.sort()

    indexlist = []
    for t in table_sorted:
        index1 = table.index(t)
        index1 = index1 + 1 if index1 < len(text) - 1 else 0
        index2 = table_sorted.index(table[index1])
        indexlist.append(index2)

    r = ''.join([row[-1] for row in table_sorted])
    return r

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
