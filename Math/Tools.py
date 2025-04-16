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






def Transpose(matrice : list[list[float]]) -> list[list[float]]: 
    mTranspose : list[list[float]] = []

    for i in range(len(matrice[0])):   
        mTranspose.append([])
        for j in range(len(matrice)):
            mTranspose[i].append(matrice[j][i])

    return mTranspose


def Ligne(n,xmin,xmax):
    W=[]
    dx=(xmax-xmin)/(n-1)
    for x in range (n):
        W.append([x*dx,0,0])
    return(Transpose(W))


def CarreVide(n : int, a : int):
    W = []
    dx = a/(n-1)
    for x in range(n):
        W.append([x*dx - a/2,0,0])
        W.append([x*dx - a/2,a,0])
        W.append([0 - a/2,x*dx,0])
        W.append([a - a/2,x*dx,0])
    return (Transpose(W))
    
def CarrePlein(n : int, a : int, z : int):
    W = []
    dx = a/(n-1)
    for x in range(int(n**(1/2))):
        for y in range(int(n**(1/2))):
            W.append([x*dx,y*dx,z])
    return (Transpose(W))

def RectanglePlein(n : int, a : int, b : int, z : int):
    W = []
    dx = a/(n-1)
    dy = b/(n-1)
    for x in range(int(n**(1/2))):
        for y in range(int(n**(1/2))):
            W.append([-b/2+x*dx,y*dy,z])
    return (Transpose(W))

def PavePlein(n : float, largeur : int, longueur : int, hauteur : int):

    points_par_axe =  int(n**(1/3))

    dx = largeur / (points_par_axe - 1)
    dy = longueur / (points_par_axe - 1)
    dz = hauteur / (points_par_axe - 1)

    points = []

    for i in range(points_par_axe):
        for j in range(points_par_axe):
            for k in range(points_par_axe):
                x = -largeur / 2 + i * dx
                y = -longueur / 2 + j * dy
                z = -hauteur / 2 + k * dz
                points.append([x, y, z])

    return Transpose(points)

def CerclePlein(n : int, r : int, t :int, p :int):
    W = []
    dr = r/(n-1)

    precision : int = int(n//t)

    for k in range (1,t+1):
        for i in range(0,precision):
            W.append([(dr * i * t/2 * tools.cos(2*3.14/(t/k), 10)), (dr * i * t/2 * tools.sin(2*3.14/(t/k), 10)), p])
        

    return (Transpose(W))

def CylindrePlein(n : int, r : int, t : int, h : int):
    
    W = []

    dr = r/(n-1)
    for k in range(h):
        #W.append(CerclePlein(n/h,r,t,k-(h/2)))
        precision : int = int((n//t)/h)
        for j in range (1,t+1):
            for i in range(0,precision):
                W.append([(dr * i * t/2 * tools.cos(2*3.14/(t/j), 10)), (dr * i * t/2 * tools.sin(2*3.14/(t/j), 10)), k-(h/2)])

    return (Transpose(W))