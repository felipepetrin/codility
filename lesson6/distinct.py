def solution(A):
    return len(set(A))


if __name__ == "__main__":
    distinct = [0, 3, 2, 5, 4, 3, 0]
    print(solution(distinct))
