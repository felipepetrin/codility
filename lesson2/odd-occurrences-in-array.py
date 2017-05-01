from functools import reduce


def my_solution(A):
    # write your code in Python 2.7
    for i in range(len(A)):
        temp = A[i]
        A[i] = -1
        if temp not in A:
            return temp
        A[i] = temp


def solution(A):
    # write your code in Python 2.7
    for value in A:
        if value not in A:
            return value


def community_solution(A):
    return reduce(lambda x, y: x ^ y, A)


if __name__ == "__main__":
    test = community_solution([9, 3, 9, 3, 7, 9])
    print(test)
