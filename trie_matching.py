# python3
import sys

def match_prefix_trie(text, trie):
    last_index = len(text) - 1
    current_index = 0
    symbol = text[0]
    current_level = trie[0]

    while True:
        if symbol in current_level:
            if current_level[symbol] not in trie or not any(trie[current_level[symbol]]):
                return True
            elif current_index is last_index:
                return False
            else:
                current_level = trie[current_level[symbol]]
                current_index += 1
                symbol = text[current_index]

        else:
            return False

def match_trie(text, trie):
    matches = []
    current_text = text
    index = 0

    while len(current_text) > 0:
        result = match_prefix_trie(current_text, trie)

        if result == True:
            matches.append(index)

        index += 1
        current_text = current_text[1:]

    return matches

def build_trie(patterns):
    tree = dict()
    current_node = 0
    tree[current_node] = {}

    for pattern in patterns:
        current_leaf = tree[0]

        for index in range(len(pattern)):
            current_symbol = pattern[index]

            if current_symbol in current_leaf.keys():
                current_leaf = tree[current_leaf[current_symbol]]
            else:
                current_node += 1
                current_leaf[current_symbol] = current_node
                tree[current_node] = {}
                current_leaf = tree[current_node]

    return tree

def solve(text, n, patterns):
    trie = build_trie(patterns)
    return match_trie(text, trie)

text = sys.stdin.readline().strip()
n = int (sys.stdin.readline().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve(text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
