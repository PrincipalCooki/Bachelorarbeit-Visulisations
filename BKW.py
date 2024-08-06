import numpy as np


def reduce_basis(matrix, q):
    return np.mod(matrix, q)


def add_vectors_mod_q(v1, v2, q):
    return np.mod(v1 + v2, q)


def bkw_step(A, b, q, l):
    rows, cols = A.shape
    buckets = {}

    for i in range(rows):
        key = tuple(A[i, :l])
        if key in buckets:
            buckets[key].append(i)
        else:
            buckets[key] = [i]

    for key, indices in buckets.items():
        if len(indices) > 1:
            i1, i2 = indices[0], indices[1]
            A[i2] = add_vectors_mod_q(A[i1], A[i2], q)
            b[i2] = (b[i1] + b[i2]) % q

    return A, b


def bkw(A, b, q, l):
    A = reduce_basis(A, q)
    b = np.mod(b, q)

    for i in range(A.shape[1] // l):
        A, b = bkw_step(A, b, q, l)

    return A, b


if __name__ == "__main__":
    q = 23
    l = 3

    A = np.array([
        [2, 3, 5, 7, 11],
        [4, 6, 8, 10, 12],
        [1, 9, 11, 13, 17],
        [3, 5, 7, 11, 13],
    ])
    b = np.array([1, 2, 3, 4])

    A_reduced, b_reduced = bkw(A, b, q, l)
    print("Reduced matrix A:")
    print(A_reduced)
    print("Reduced vector b:")
    print(b_reduced)
