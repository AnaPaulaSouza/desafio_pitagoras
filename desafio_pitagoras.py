#!/bin/python3

def min_max_sum(arr):

    min_value = None

    max_value = None

    total_value = 0

    for x in arr:

        if min_value is None or x < min_value:
            min_value = x

        if max_value is None or x > max_value:
            max_value = x

        total_value += x

    return total_value - max_value, total_value - min_value


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(' '.join(map(str, min_max_sum(arr))))
