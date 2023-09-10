def shell_sort(A, n):
    d = n // 2
    while d >= 1:
        for i in range(d, n):
            j = i
            v = A[i]
            while j >= d and A[j - d] > v:
                A[j] = A[j - d]
                j -= d
            A[j] = v
        d //= 2


l = [8, 9, 11, 7, 25, 3, 15, 6, 4, 0, 1, 5, 2, 13, 12, 18]

shell_sort(l, len(l))
print(l)
