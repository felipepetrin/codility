def solution(N, A):
    counters = [0] * N
    max_value = 0
    for operation in A:
        if operation <= N:
            counters[operation - 1] += 1
            max_value = max(max_value, counters[operation - 1])
        else:
            counters = [max_value] * N
    return counters


if __name__ == "__main__":
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(5, A))
