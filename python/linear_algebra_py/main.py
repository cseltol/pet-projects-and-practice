import numpy as np


def main():
    A_1 = np.matrix('1. -3.; 2. 5.')
    A_1_inv = np.linalg.inv(A_1)
    A_1_inv_inv = np.linalg.inv(A_1_inv)
    # print(f'{A_1}\n\n {A_1_inv_inv}\n\n')

    A_2 = np.matrix('1. -3; 2. 5.')
    L_2 = np.linalg.inv(A_2.T)
    R_2 = (np.linalg.inv(A_2)).T
    # print(f'{L_2}\n\n {R_2}\n\n')

    A_3 = np.matrix('1. -3.; 2. 5.')
    B_3 = np.matrix('7. 6.; 1. 8.')
    L_3 = np.linalg.inv(A_3.dot(B_3))
    R_3 = np.linalg.inv(B_3).dot(np.linalg.inv(A_3))
    # print(f'{L_3}\n\n {R_3}\n\n')

    m_eye = np.eye(4)
    # print(m_eye, end='\n\n')

    rank = np.linalg.matrix_rank(m_eye)
    # print(rank)

    A_4 = np.matrix('3 -1 2; 1 4 -1; 2 3 1')
    B_4 = np.matrix('-4; 10; 8')
    # print(f'{A_4}\n\n {B_4}\n\n')
    A_4_inv = np.linalg.inv(A_4)
    # print(A_4_inv, end='\n\n')
    X_4 = A_4_inv.dot(B_4)
    # print(X_4, end='\n\n')

    # 49 page


if __name__ == '__main__':
    main()
