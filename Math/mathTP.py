import matplotlib.pyplot as plt
import Tools as tools

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

def PavePlein(n : int, a : int, b : int, c : int):
    W = []
    for h in range(c):
        W.append(RectanglePlein(n/c,a,b,h))
    return (Transpose(W))


def CerclePlein(n : int, r : int, t :int, p :int):
    W = []
    dr = r/(n-1)

    precision : int = int(n//t)

    for k in range (1,t+1):
        for i in range(0,precision):
            W.append([(dr * i * t/2 * cos(2*3.14/(t/k), 10)), (dr * i * t/2 * sin(2*3.14/(t/k), 10)), p])
        

    return (Transpose(W))

def CylindrePlein(n : int, r : int, t : int, h : int):
    
    W = []
    for k in range(h):
        W.append(CerclePlein(n/h,r,t,k-(h/2)))
    return (Transpose(W))


if __name__ == '__main__':
    # m = [[-1,2],[0,1],[3,4]]

    # newM = Transpose(m)


    # # Définition des lignes de traçage
    # #(X,Y,Z)=CarreVide(20,10)
    # #(X,Y,Z)=CarrePlein(20,10,0)
    # #(X,Y,Z)=PavePlein(5000,50,5,20)
    # #(X,Y,Z)=CerclePlein(500,5,100,0)
    (X,Y,Z)=CylindrePlein(10000,5,30,40)


    print(X[20][0])
    print(Y[20][0])
    print(Z[20][0])
    # Init plt
    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
    # plt.show()

    F: list[list[list[float]]] = [[[0,0,10],[1,0,-2]],[[0,0,5],[-1,0,-2]],[[-2,0,0],[1,0,0]]]
    m = 20

    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
    # plt.show()