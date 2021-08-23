def findRotation(mat, target):
    N = len(mat)
    print(flip_horizontal(mat, N))
    # if flip_horizontal(transpose_matrix(mat, N), N) == target:
    #     return True
    # else:
    #     return False


def transpose_matrix(matrix, N):
    for i in range(0, N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def flip_horizontal(matrix, N):
    for i in range(0, N):
            for j in range(i, int(N / 2)):
                matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
    return matrix


if __name__ == '__main__':
    findRotation([[0,1],[1,0]], [[1,0],[0,1]])
