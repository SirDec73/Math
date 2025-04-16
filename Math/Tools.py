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


def factoriel(n : int):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def cos(x : float,n : int):
    result = 0
    for k in range(0,n+1):
        result += ((-1)**k) * ((x ** (2 * k)) / factoriel(2 * k))
    return result

def sin(x : float,n : int):
    result = 0
    for k in range(0,n+1):
        result += (-1)**k * (x**(2*k+1))/factoriel(2*k+1)
    return result

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


def multiplier_matrice_point(matrice, point):
    resultat = [
        matrice[0][0] * point[0] + matrice[0][1] * point[1] + matrice[0][2] * point[2],
        matrice[1][0] * point[0] + matrice[1][1] * point[1] + matrice[1][2] * point[2],
        matrice[2][0] * point[0] + matrice[2][1] * point[1] + matrice[2][2] * point[2],
    ]

    return resultat


def A_Prod_InverseA(A: list):
    InverseA: list = InverseMatrice(A)

    return Prod_Matrice_A__Matrice_B(A, InverseA)



def Somme2List(A: list, B: list):
    return  [(A[0] + B[0]), (A[1] + B[1]), (A[2] + B[2])]

