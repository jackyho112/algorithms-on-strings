# python3
import sys

def InverseBWT(bwt):
    combos = [(value, index) for (index, value) in enumerate(bwt)]

    sorted_combos = sorted(combos)
    transformed_combos = {
        form: letter for form, letter in zip(sorted_combos, combos)
    }

    next_string = sorted_combos[0]
    result = ''

    for i in range(len(bwt)):
        result += next_string[0]
        next_string = transformed_combos[next_string]

    return result[::-1]

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
