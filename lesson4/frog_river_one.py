def solution(X, A):
    counter = [0] * X
    index = 0
    for value in A:
        if value <= X:
            counter[value - 1] = 1
        if 0 not in counter:
            return index
        index += 1
    return -1


if __name__ == "__main__":
    leaves = [1, 3, 7, 4, 2, 3, 5, 4]
    print(solution(5, leaves))
