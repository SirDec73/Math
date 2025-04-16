import matplotlib.pyplot as plt
import matplotlib.animation as anim
import Tools as tools
import TP3Math as tp3



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


def deplace_mat(I: list[list[float]], m: float, G: list[float], A: list[float]):
    tmpM: list[list[float]] = []
    matriceA: list[list[float]] = []
    
    for i in range(3):
        tmp = [0, 0, 0]
        tmpM.append(tmp)
        matriceA.append(tmp)
        
    
    vectAG: list = [A[0] - G[0], A[1] - G[1], A[2] - G[2]]
    
    ab: float = vectAG[0] * vectAG[1]
    ac: float = vectAG[0] * vectAG[2]
    bc: float = vectAG[1] * vectAG[2]
    
    
    tmpM[0][1] = tmpM[1][0] = -m*ab        
    tmpM[0][2] = tmpM[2][0] = -m*ac        
    tmpM[1][2] = tmpM[2][1] = -m*bc
    
    
    tmpM[0][0] = m * (vectAG[1]**2 + vectAG[2]**2)
    tmpM[1][1] = m * (vectAG[0]**2 + vectAG[2]**2)
    tmpM[2][2] = m * (vectAG[0]**2 + vectAG[1]**2)
    
    
    matriceA[0] = [I[0][0] + tmpM[0][0], I[0][1] + tmpM[0][1], I[0][2] + tmpM[0][2]]
    matriceA[1] = [I[1][0] + tmpM[1][0], I[1][1] + tmpM[1][1], I[1][2] + tmpM[1][2]]
    matriceA[2] = [I[2][0] + tmpM[2][0], I[2][1] + tmpM[2][1], I[2][2] + tmpM[2][2]]
    
    
    return matriceA


def translateSkate(X: list, Y: list, Z: list, F, m, h):
    vG=[0,0,0]

    newW= (X,Y,Z)
    newG=G
    newvG=vG
    
    for i in range(n):
        (X,Y,Z)=newW
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
        ax.axes.set_xlim3d(left=-70, right=70)
        ax.axes.set_ylim3d(bottom=-70, top=70)
        ax.axes.set_zlim3d(bottom=-7, top=7)
        plt.show()
        (newG,newvG)=tp3.translation(m,F,newG,newvG,h)
        newW=tp3.translate((X,Y,Z),G,newG)



def rotateSkate(X: list, Y: list, Z: list, F, G, h):
    vG=[0,0,0]

    newW= (X,Y,Z)
    omega= [0, 0, 0]
    Teta= [0,0, 0]
    
    for i in range(n):
        (X,Y,Z)=newW
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
        ax.axes.set_xlim3d(left=-70, right=70)
        ax.axes.set_ylim3d(bottom=-70, top=70)
        ax.axes.set_zlim3d(bottom=-7, top=7)
        plt.show()
        (omega,Teta)=tp3.rotation((X,Y,Z),F, G,Teta,omega,h)
        newW=tp3.rotate((X,Y,Z),Teta)


if __name__ == '__main__':
    
    m1 = 1
    m2 = 1
    m3 = 1
    m4 = 1
    
    mTotal = m1 + 4*m2 + 2*m3 + 2*m4
    
    L1 = 21
    l1 = 80
    E1 = 1
    
    R2 = 2.75
    H2 = 2.5
    
    R3 = 1
    H3 = 15
    
    L4 = 7.5
    l4 = 5.5
    E4 = 6.5
    
    GsystemZ = ((m2 * (-(E1 + E4) / 2 - R3) * 4) + (m3 * (-(E1 + E4) / 2 -R3) * 2) + (m4 * (-(E1 + E4)) / 2) *2) / mTotal
    
    _11 = (1/12)*(m1*(L1**2 + E1**2) + m2*(3*(R2**2) + H2**2) + m3*(3*(R3**2) + H3**3) + m4*(L4**2 + E4**2)) + (mTotal * GsystemZ**2)
    _22 = (1/12)*(m1*(l1**2 + E1**2) + m4*(l4**2 + E4**2)) + (1/2)*(m2 * (R2**2) + m3 * (R3**2))  + (mTotal * GsystemZ**2)
    _33 = (1/12)*(m1*(l1**2 + L1**2) + m2*(3*(R2**2) + H2**2) + m3*(3*(R3**2) + H3**3) + m4*(l4**2 + L4**2))
    
    Ig = [[_11, 0, 0], [0, _22, 0], [0, 0, _33]]
    
    G = [0, 0, 0]
    
    F: list[list[list[float]]] = [[[0,0,-9.81],[0,0,0]], [[0,0,-120/mTotal],[0, 80/4, 1/2]]]  
    
    newI : list[list[float]]
    
    #newI = deplace_mat(Ig, mTotal ,G, A)
    
    #print(newI)
    
    tmax=5
    n=10
    h=tmax/n
    
    (X,Y,Z) = Solide(5000)
    #translateSkate(X, Y, Z, F, mTotal, h) 
    
    rotateSkate(X, Y, Z, F, G, h)
          
         


    #N = 10 / 100
    #t: list = []
    #y: list = []
    #
    #for i in range(100):
    #    t.append(N)
    #    N+= 0.1
    #    y.append(sin(t[i], 20))
    
    
    ##fig, axis = plt.subplots()
    #(X,Y,Z)=newW
    #fig = plt.figure()
    #ax = plt.axes(projection='3d')
    #ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
    #ax.axes.set_xlim3d(left=-5, right=5)
    #ax.axes.set_ylim3d(bottom=-5, top=5)
    #ax.axes.set_zlim3d(bottom=-5, top=5) 
    #
    #x: list[list[float]] = []
    #y: list[list[float]] = []
    #z: list[list[float]] = []
    #
    #    
    #animated_plot, = ax.plot([], [], [])
    #
    #
   #
    #for i in range(10):        
    #    (newG,newvG)=tp3.translation(m,F,newG,newvG,h)
    #    newW=tp3.translate(W,G,newG)
    #    
    #    x.append(newW[0])
    #    y.append(newW[1])
    #    z.append(newW[2])
    #
    #def AnimationTranslate(frame):
    #    
    #    animated_plot.set_data(x[:frame], y[:frame], z[:frame])
    #
    #    return animated_plot,
    #
    #
    #animation = anim.FuncAnimation(fig=fig, func=AnimationTranslate, frames=len(x), interval=25)
    #
    #
    #plt.show()
    
    
    