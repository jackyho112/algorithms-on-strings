# python3
import sys

def build_pattern_suffixes(pattern):
    result = []
    result.append(0)
    border = 0
    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = result[border - 1]

        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0

        result.append(border)
    return result

def find_pattern(pattern, text):
    pattern_length = len(pattern)
    string = pattern + '$' + text
    suffixes = build_pattern_suffixes(string)
    result = []

    for i in range(pattern_length, len(string)):
        if suffixes[i] == pattern_length:
            result.append(i - 2 * pattern_length)

    return result

if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
