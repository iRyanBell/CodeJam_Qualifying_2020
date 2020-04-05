# Vestigium
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

import numpy as np

t = int(input())
for i in range(1, t + 1):
    N = int(input())
    M = []
    k = 0  # Sum along TL->BR Diagonal
    r = 0  # Repeated row values
    c = 0  # Repeated col values
    for j in range(N):
        M.append([x for x in map(int, input().strip().split())])
        k += M[j][j]
        if len(M[j]) - len(set(M[j])) > 0:  # Duplicate rows
            r += 1

    M_T = np.array(M).T.tolist()  # Transposed rows -> cols
    for j in range(N):
        if len(M_T[j]) - len(set(M_T[j])) > 0:  # Duplicate cols
            c += 1

    print("Case #{}: {} {} {}".format(i, k, r, c))
