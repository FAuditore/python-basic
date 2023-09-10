def merge(A, p, q, r):
    left = p
    right = q + 1
    k = p
    seen = -1

    for i in range(p, r + 1):
        B[i] = A[i]

    while left <= q and right <= r:
        # 跳过-1和重复元素
        if B[left] == -1 or B[left] == seen:
            left += 1
            continue
        if B[right] == -1 or B[right] == seen:
            right += 1
            continue
        if B[left] < B[right]:
            A[k] = B[left]
            seen = A[k]
            left += 1
        else:
            A[k] = B[right]
            seen = A[k]
            right += 1

        k += 1

    while left <= q:
        A[k] = B[left]
        k, left = k + 1, left + 1

    while right <= r:
        A[k] = B[right]
        k, right = k + 1, right + 1

    while k <= r:
        A[k] = -1
        k += 1


def merge_sort(arr, p, r):
    if p < r:
        m = p + (r - p) // 2
        merge_sort(arr, p, m)
        merge_sort(arr, m + 1, r)
        merge(arr, p, m, r)


A = [1, 1, 4, 3, 5, 7, 2, 2, 2]
B = [-1] * len(A)

merge_sort(A, 0, len(A) - 1)

print(A)  # [1, 2, 3, 4, 5, 7, -1, -1, -1]
