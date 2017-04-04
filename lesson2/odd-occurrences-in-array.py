def solution(A):
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


if __name__ == "__main__":
    test = solution([9, 3, 9, 3, 7, 9])
    print(test)
