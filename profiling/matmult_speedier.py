import numpy as np

N = 250

@profile
def make_data(N):
    X = np.random.randint(0, 101, size=(N, N))
    Y = np.random.randint(0, 101, size=(N, N + 1))
    return X, Y
@profile
def matmul_fast(X, Y):
    return X @ Y  # or np.matmul(X, Y)

X, Y = make_data(N)
result = matmul_fast(X, Y)

