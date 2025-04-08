# import plt

def pop(A: list, i: int, j: int):
    B: list = []
    n = len(A)

    for k in range(n):
        if k != i:
            C: list = []
            for l in range(n):
                if l != j:
                    C.append(A[k][l])
            B.append(C)
    return B


def determinant(A: list):
    n = len(A)
    S = 0
    j = 0

    if n == 1:
        return A[0][0]

    for i in range(n):
        S += ((-1)**(i+j)) * A[i][j] * determinant(pop(A, i, j))

    return S



def DeltaMatrice(A: list, i: int, j: int):
    return ((-1)**(i+j)) * determinant(pop(A, i, j))



def Comatrice(A: list):
    B: list = []
    n = len(A)

    for i in range(n):
        C: list = []
        for j in range(n):
            C.append(DeltaMatrice(A, i, j))
        B.append(C)

    return B


def Transpose(matrice: list):
    transpose: list = []

    for i in range(len(matrice[0])):
        transpose.append([])
        for j in range(len(matrice)):
            transpose[i].append(matrice[j][i])

    return transpose


def Matrice_Prod_Scalaire(A: list, k: int):
    B: list = []
    n: int = len(A)

    for i in range(n):
        C: list = []
        for j in range(n):
            C.append((A[i][j] * k))
        B.append(C)
    return B



def InverseMatrice(A: list):
    return Matrice_Prod_Scalaire(Transpose(Comatrice(A)), (1 / determinant(A)))


def Prod_Matrice_A__Matrice_B(A: list, B: list):
    C: list = []
    n: int = len(A)

    for i in range(n):
        D: list = []
        for j in range(n):
            h: int = 0
            for k in range(n):
                h += A[i][k] * B[k][j]
            D.append(h)
        C.append(D)

    return C


def A_Prod_InverseA(A: list):
    InverseA: list = InverseMatrice(A)

    return Prod_Matrice_A__Matrice_B(A, InverseA)




def main():
    A: list = [[1, 2, 3], [44, 5, 6], [7, 8, 9]]
    Z: list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    B: list = A_Prod_InverseA(Z)

    print(B)

main()