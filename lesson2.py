# coding: utf-8


def my_reverse(array):
    first = 0
    last = len(array) - 1
    while first < last:
        array[first], array[last] = array[last], array[first]
        first += 1
        last -= 1
    print(array)


# Solução proposta pelo exercicio
def reverse(array):
    N = len(array)
    for i in range(N // 2):
        k = N - i - 1
        array[i], array[k] = array[k], array[i]
    print(array)


if __name__ == "__main__":
    my_reverse([1, 2, 3, 4, 5])
    reverse([1, 2, 3, 4, 5])
