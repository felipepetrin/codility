def solution(A):
    result = 1
    A = set(A)
    while result in A:
        result += 1

    return result


if __name__ == "__main__":
    array = [1, 3, 6, 4, 1, 2]
    print(solution(array))
