def merge(A, m, B, n):
    # write your solution here
     C = []
    A_more = len(A) - m
    B_more = len(B) - n
    A = A[:len(A) - A_more]
    B = B[:len(B) - B_more]

    while m > 0 and n > 0:
        if A[0] <= B[0]:
            C.append(A[0])
            A.pop(0)
            m = m - 1
        else:
            C.append(B[0])
            B.pop(0)
            n = n - 1

    if m == 0:
        C.extend(B)
    if n == 0:
        C.extend(A)

    return C