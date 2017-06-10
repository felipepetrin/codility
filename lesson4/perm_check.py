def solution(A):
    length = len(A)
    return int(max(A) == length and len(set(A)) == length)


if __name__ == "__main__":
    permutation = [1, 2, 4, 5, 4]
    print(solution(permutation))
