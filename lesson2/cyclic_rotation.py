def my_solution(A, K):
    length = len(A)
    result = [0] * length

    for i, value in enumerate(A):
        i = i + K
        if i >= length:
            i -= length
        result[i] = value
    return result


def other_solution(A, K):
    length = len(A)

    if length == 0:
        return A

    result = [0] * length
    rotation = K % length

    for i, value in enumerate(A):
        i += rotation
        if i >= length:
            i -= length
        result[i] = value
    return result


if __name__ == "__main__":
    array = [3, 8, 9, 7, 6]
    # print(my_solution(array, 7))
    empty = []
    print(other_solution(empty, 1))
