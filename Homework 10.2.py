A = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1],
]

for pillar_index in reversed(range(7)):
    if pillar_index % 2 != 0 or A[0][pillar_index] < A[4 - 1][pillar_index]:
        for i in range(4):
            del A[i][pillar_index]
print(A[0][0], A[0][1])
print(A[1][0], A[1][1])
print(A[2][0], A[2][1])
print(A[3][0], A[3][1])
