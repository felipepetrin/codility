def my_solution(A):
    currently_sum = sum(A)
    max_value = len(A) + 1
    sum_array_should_have = max_value * (max_value + 1) // 2
    return sum_array_should_have - currently_sum


def solution(A):
    xor = len(A) + 1
    for a, i in enumerate(A, 1):
        xor = xor ^ a ^ i
    return xor


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    print(solution(array))
