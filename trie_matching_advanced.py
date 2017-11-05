# python3
import sys

class Node:
	def __init__(self):
		self.next = {}
		self.pattern_end = False

def solve(text, n, patterns):
	result = []
	root = Node()

	for pattern in patterns:
		last_index = len(pattern) - 1
		currentNode = root

		for i, char in enumerate(pattern):
			if char not in currentNode.next:
				currentNode.next[char] = Node()

			if i == last_index:
				currentNode.next[char].pattern_end = True
			else:
				currentNode = currentNode.next[char]

	for i in range(len(text)):
		index = i
		currentNode = root
		while index < len(text):
			char = text[index]

			if char not in currentNode.next:
				break

			currentNode = currentNode.next[char]

			if currentNode.pattern_end:
				result.append(i)
				break

			index += 1

	return result

text = sys.stdin.readline().strip ()
n = int (sys.stdin.readline().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline().strip ()]

ans = solve(text, n, patterns)

sys.stdout.write (' '.join (map(str, ans)) + '\n')
