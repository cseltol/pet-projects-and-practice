def rotate(matrix):
    N = len(matrix)
    print((flip_horizontal(transpose_matrix(matrix, N), N)))


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
    rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
