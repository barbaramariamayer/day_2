import random

N = 250

@profile
def make_data(N):
    X = [[random.randint(0,100) for _ in range(N)] for _ in range(N)]
    Y = [[random.randint(0,100) for _ in range(N+1)] for _ in range(N)]
    result = [[0] * (N+1) for _ in range(N)]
    return X, Y, result

@profile
def matmul(X, Y, result):
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

X, Y, result = make_data(N)
matmul(X, Y, result)

