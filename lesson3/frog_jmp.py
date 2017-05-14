def solution(X, Y, D):
    import math
    return int(math.ceil((Y - X) / float(D)))


if __name__ == "__main__":
    print(solution(5, 105, 3))
