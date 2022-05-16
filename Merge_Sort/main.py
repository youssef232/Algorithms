import math


def Merge(A: list[int], p, q, r):

    left, right = A[p: q + 1], A[q + 1 : r + 1]

    right.append(math.inf)
    left.append(math.inf)
    i = j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


def Merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        Merge_sort(A, p, q)
        Merge_sort(A, q + 1, r)
        Merge(A, p, q, r)


A = [5, 2, 4, 7, 1, 3, 2, 6]
Merge_sort(A, 0, len(A) - 1)
print(A)
