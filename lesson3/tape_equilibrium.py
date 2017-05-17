def solution(A):
    lowest_sum = 2001
    before = 0
    after = sum(A)
    for value in A[:-1]:
        before += value
        after -= value
        result = abs(before - after)
        if result < lowest_sum:
            lowest_sum = result
    return lowest_sum


if __name__ == "__main__":
    tape = [-1000, 1000]
    print(solution(tape))
