import sys


def solution(argv):
    binary = "{0:b}".format(argv)
    binary_list = list(binary)
    last_gap = 0
    current_gap = 0

    for num in binary_list:
        if num == '1':
            if current_gap > last_gap:
                last_gap = current_gap
            current_gap = 0
        else:
            current_gap += 1

    return last_gap


if __name__ == "__main__":
    gap = solution(int(sys.argv[1]))
    print(gap)
