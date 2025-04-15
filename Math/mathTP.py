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
            W.append([(dr * i * t/2 * cos(2*3.14/(t/k), 10)), (dr * i * t/2 * sin(2*3.14/(t/k), 10)), p])
        

    return (Transpose(W))

def CylindrePlein(n : int, r : int, t : int, h : int):
    
    W = []

    dr = r/(n-1)
    for k in range(h):
        #W.append(CerclePlein(n/h,r,t,k-(h/2)))
        precision : int = int((n//t)/h)
        for j in range (1,t+1):
            for i in range(0,precision):
                W.append([(dr * i * t/2 * cos(2*3.14/(t/j), 10)), (dr * i * t/2 * sin(2*3.14/(t/j), 10)), k-(h/2)])

    return (Transpose(W))

def Solide(n):
    X : list[float] = []
    Y : list[float] = []
    Z : list[float] = []

    #Planche
    (X1,Y1,Z1)=PavePlein(n*0.57,80,21,1)

    for i in range (len(X1)):
        X.append(X1[i])
        Y.append(Y1[i])
        Z.append(Z1[i])

    #Truck
    (X2,Y2,Z2)=PavePlein(n*0.09,6,8,1)
    for i in range (len(X2)):
        X2[i] += 20 
        Z2[i] -= 1 

    (X3,Y3,Z3)=PavePlein(n*0.09,6,8,1)
    for i in range (len(X3)):
        X3[i] -= 20 
        Z3[i] -= 1 
    for i in range (len(X2)):
        X.append(X2[i])
        Y.append(Y2[i])
        Z.append(Z2[i])
        X.append(X3[i])
        Y.append(Y3[i])
        Z.append(Z3[i])

    #Tige
    (X4,Y4,Z4)=PavePlein(n*0.04,0.5,15,0.1)
    for i in range (len(X4)):
        X4[i] += 20 
        Z4[i] -= 2
    
    (X5,Y5,Z5)=PavePlein(n*0.04,0.5,15,0.1)
    for i in range (len(X5)):
        X5[i] -= 20 
        Z5[i] -= 2
    for i in range (len(X5)):
        X.append(X4[i])
        Y.append(Y4[i])
        Z.append(Z4[i])
        X.append(X5[i])
        Y.append(Y5[i])
        Z.append(Z5[i])

    # ROUE
    (X6,Y6,Z6)=PavePlein(n*0.04,2,2,0.5)
    for i in range (len(X6)):
        X6[i] -= 20 
        Y6[i] -= 7.5 
        Z6[i] -= 2
    for i in range (len(X6)):
        X.append(X6[i])
        Y.append(Y6[i])
        Z.append(Z6[i])
               
    for i in range (len(X6)):
        X6[i] += 40 
    for i in range (len(X6)):
        X.append(X6[i])
        Y.append(Y6[i])
        Z.append(Z6[i])
    for i in range (len(X6)):
        Y6[i] += 15 
    for i in range (len(X6)):
        X.append(X6[i])
        Y.append(Y6[i])
        Z.append(Z6[i])
    for i in range (len(X6)):
        X6[i] -= 40 
    for i in range (len(X6)):
        X.append(X6[i])
        Y.append(Y6[i])
        Z.append(Z6[i])
        
    print(len(X))
    return(X,Y,Z)

if __name__ == '__main__':
    
    (X,Y,Z) = Solide(5000)
    F: list[list[list[float]]] = [[[0,0,10],[1,0,-2]],[[0,0,5],[-1,0,-2]],[[-2,0,0],[1,0,0]]]
    m = 20

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
    ax.axes.set_xlim3d(left=-50, right=50) 
    ax.axes.set_ylim3d(bottom=-50, top=50) 
    ax.axes.set_zlim3d(bottom=-7, top=7)
    plt.show()