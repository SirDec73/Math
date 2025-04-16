import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Tools as tools
import TP3Math as tp3



def Solide(n):
    X : list[float] = []
    Y : list[float] = []
    Z : list[float] = []

    #Planche
    (X1,Y1,Z1)=tools.PavePlein(n*0.57,80,21,1)

    for i in range (len(X1)):
        X.append(X1[i])
        Y.append(Y1[i])
        Z.append(Z1[i])

    #Truck
    (X2,Y2,Z2)=tools.PavePlein(n*0.09,6,8,1)
    for i in range (len(X2)):
        X2[i] += 20 
        Z2[i] -= 1 

    (X3,Y3,Z3)=tools.PavePlein(n*0.09,6,8,1)
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
    (X4,Y4,Z4)=tools.PavePlein(n*0.04,0.5,15,0.1)
    for i in range (len(X4)):
        X4[i] += 20 
        Z4[i] -= 2
    
    (X5,Y5,Z5)=tools.PavePlein(n*0.04,0.5,15,0.1)
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
    (X6,Y6,Z6)=tools.PavePlein(n*0.04,2,2,0.5)
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
        ax.axes.set_xlim3d(left=-50, right=50)
        ax.axes.set_ylim3d(bottom=-50, top=50)
        ax.axes.set_zlim3d(bottom=-50, top=50)
        plt.show()
        (newG,newvG)=tp3.translation(m,F,newG,newvG,h)
        newW=tp3.translate((X,Y,Z),G,newG) 



def rotateSkate(X: list, Y: list, Z: list, F, G, Ig, h):
    vG=[0,0,0]

    newW= (X,Y,Z)
    omega= [0, 0, 0]
    Teta= [0,0, 0]
    
    for i in range(n):
        (X,Y,Z)=newW
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
        ax.axes.set_xlim3d(left=-50, right=50)
        ax.axes.set_ylim3d(bottom=-50, top=50)
        ax.axes.set_zlim3d(bottom=-50, top=50)
        plt.show()
        (omega,Teta)=tp3.rotation(Ig,F, G,Teta,omega,h)
        newW=tp3.rotate((X,Y,Z),Teta)
        

def mouvement(X: list[float],
              Y: list[float],
              Z: list[float], 
              m : float, 
              I :list[list[float]], 
              F:list[list[list[float]]], 
              G : list[float], 
              vG : list[float], 
              omega : list[float], 
              t : float, 
              n : int):
    
    newG=G
    newvG=vG

    newW= (X,Y,Z)
    Teta= [0,0,0]
    
    G0 = [0,0,0]

    for i in range(n):
        
        (newG,newvG)=tp3.translation(m,F,newG,newvG,t)
        newW=tp3.translate(newW,G,newG)
        G = newG
        print(newG)

        for i in range(len(newW[0])):
            newW[0][i] = newW[0][i] - newG[0]
            newW[1][i] = newW[1][i] - newG[1]
            newW[2][i] = newW[2][i] - newG[2]

        (omega,Teta)=tp3.rotation(I,F, G0,Teta,omega,t)
        newW=tp3.rotate(newW,Teta)

        for i in range(len(newW[0])):
            newW[0][i] = newW[0][i] + newG[0]
            newW[1][i] = newW[1][i] + newG[1]
            newW[2][i] = newW[2][i] + newG[2]

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(newW[0], newW[1], newW[2], c=Z, cmap='ocean')
        ax.axes.set_xlim3d(left=-100, right=100)
        ax.axes.set_ylim3d(bottom=-100, top=100)
        ax.axes.set_zlim3d(bottom=-200, top=0)
        plt.show()

    return 0


def mouvementAnime(X, Y, Z, m, I, F, G, vG, omega, tmax, n):
    newG = G
    newvG = vG
    newW = (X, Y, Z)
    Teta = [0, 0, 0]
    G0 = [0, 0, 0]
    
    
    h=tmax/n

    positions = []

    for i in range(n):
        newG, newvG = tp3.translation(m, F, newG, newvG, h)
        newW = tp3.translate(newW, G, newG)
        G = newG

        for j in range(len(newW[0])):
            newW[0][j] -= newG[0]
            newW[1][j] -= newG[1]
            newW[2][j] -= newG[2]

        omega, Teta = tp3.rotation(I, F, G0, Teta, omega, h)
        newW = tp3.rotate(newW, Teta)

        for j in range(len(newW[0])):
            newW[0][j] += newG[0]
            newW[1][j] += newG[1]
            newW[2][j] += newG[2]

        positions.append((list(newW[0]), list(newW[1]), list(newW[2])))

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    scat = ax.scatter([], [], [], c='blue', s=1)

    ax.set_xlim3d(-100, 100)
    ax.set_ylim3d(-100, 100)
    ax.set_zlim3d(-200, 0)

    def update(frame):
        Xf, Yf, Zf = positions[frame]
        scat._offsets3d = (Xf, Yf, Zf)
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=len(positions), interval=50,)
    plt.show()


if __name__ == '__main__':   

    #m1 = 1 # Planche
    #m2 = 1 # Roue
    #m3 = 1 # Tige
    #m4 = 1 # Truck


    m1 = 1.176 # Planche
    m2 = 0.071 # Roue
    m3 = 0.127 # Tige
    m4 = 0.72  # Truck
    
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
    
    vG : list[float] = [0,0,0]
    omega : list[float] = [0,0,0]
    
    tmax=5
    n=100
    
    (X,Y,Z) = Solide(5000)
          
    mouvementAnime(X, Y, Z,mTotal,Ig,F,G,vG,omega,tmax,n)    
    
    