def LU(A):

    n = len(A) 
    b = [0] * n
    for i in range(0, n):
        b[i] = A[i][n-1]

    
    L = [[0 for i in range(n)] for i in range(n)]
    for i in range(0, n):
        L[i][i] = 1

    
    U = [[0 for i in range(0, n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            U[i][j] = A[i][j]

    n = len(U)

    for i in range(0, n):  
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i+1, n):
            if(abs(U[k][i]) > maxElem):
                maxElem = abs(U[k][i])
                maxRow = k

        for k in range(i, n):
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp

        for k in range(i+1, n):
            c = -U[k][i]/float(U[i][i])
            L[k][i] = c 
            for j in range(i, n):
                U[k][j] += c*U[i][j]

        
        for k in range(i+1, n):
            U[k][i] = 0

    return L, U


def print_matrix(mat):
    N = len(mat)
    M = len(mat[0])
    for i in range(N):
        print("|", end=" ")
        for j in range(M):
            print("%2.2f " % mat[i][j], end=" ")
        print(" |")



A = [[2, -1, 1], [3, 3, 9], [3, 3, 5]]

if __name__ == '__main__':
    L, U = LU(A)
    print("\nL Matrix")
    print_matrix(L)
    print("\nU Matrix")
    print_matrix(U)
