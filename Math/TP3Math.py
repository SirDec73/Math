import Tools as tools

def SommeList(L1: list[float],L2: list[float]):
    L3: list = []
    for i in range(len(L1)):
        L3.append(L1[i]+L2[i])
    return L3

def prod_vect_scal(A,k):
    B=[]
    for i in range (len(A)):
        B.append(k*A[i])
    return(B)

def vect(A,B):
    return(SommeList(prod_vect_scal(A,-1),B))


def Derive(v_2:list[float],a_1:list[float],h:float):
    return SommeList(a_1 * h, v_2) 


# def Translation(m:float,F:list[list[list[float]]],G:list[list[list[float]]],vG:list[float,float,float],h:float): 

#     #Calcul somme des forces
#     sommeAcc : list[float] = [0,0,0]
#     for i in range(len(F)):
#         sommeAcc = SommeList(sommeAcc,F[i][0]) 
#     sommeForce: list[float]  = sommeAcc * m

#     #Calcul nouvelle vitesse
#     new_vG : list[float] = Derive(vG,sommeForce,h)

#     #Calcul nouvelle position
#     # for i in range(len(G)):
#     #     for j in range(len(G[i])):
#     #         for k in range(len(G[i])):
#     #             G[i][j][k] = Derive(G[i][j][k],new_vG,h)
#     for k in range(len(G[i])):
#         G[20][0][k] = Derive(G[0][0][k],new_vG,h)
    
#     new_G :list[list[list[float]]] = G
#     return new_vG, new_G



def translation(m,F,G,vG,h):
    SF=[0,0,0]
    for i in range(len(F)):
        SF=SommeList(SF,F[i][0])
        aG=prod_vect_scal(SF,1/m)
        newG=SommeList(G,prod_vect_scal(vG,h))
        newvG=SommeList(vG,prod_vect_scal(aG,h))
    return(newG,newvG)


def translate(W,G,newG):
    newW=[]
    GnewG=vect(G,newG)
    for i in range(len(W[0])):
        newW.append(SommeList([W[0][i],W[1][i],W[2][i]],GnewG))
    return(tools.Transpose(newW))


def prod_vect(A, B):
    x1, y1, z1 = A
    x2, y2, z2 = B
    
    produit = (
        y1 * z2 - z1 * y2,  
        z1 * x2 - x1 * z2,  
        x1 * y2 - y1 * x2  
    )
    
    return produit


def rotation(I: list[list[float]], F: list[list[list[float]]], G: list[float], teta: list[float], omega: list[float], h: float):
    SM = [0, 0, 0]
    for i in range(len(F)):
        aG =vect(G, F[i][1])
        Mg: list = prod_vect(aG,F[i][0])
        SM=SommeList(SM, Mg)
        
        
    MatMg = [[SM[0], 0, 0], [0, SM[1], 0], [0, 0, SM[2]]]
    
    Inverse = tools.InverseMatrice(I)
    print("Omega")
    print(omega)
    omega2=prod_vect_scal(omega, h)
    newTeta = tools.Somme2List(teta, omega2)
    
    print("Omega2")
    print(omega2)
    newomega = tools.multiplier_matrice_point(Inverse, SM)
    print("newOmega")
    print(omega2)
    
    
    return (newomega, newTeta)
    

def rotate(W, teta):
    newW=[[],[],[]]
    precision = 10
    Mox = [[1, 0, 0], [0, tools.cos(teta[0], precision), -tools.sin(teta[0], precision)], [0, tools.sin(teta[0], precision), tools.cos(teta[0], precision)]]
    Moy = [[tools.cos(teta[1], precision), 0, -tools.sin(teta[1], precision)], [0, 1, 0], [tools.sin(teta[1], precision), 0, tools.cos(teta[1], precision)]]
    Moz = [[tools.cos(teta[2], precision), -tools.sin(teta[2], precision), 0], [tools.sin(teta[2], precision), tools.cos(teta[2], precision), 0], [0, 0, 1]]
    
    M = tools.Prod_Matrice_A__Matrice_B(tools.Prod_Matrice_A__Matrice_B(Mox, Moy), Moz)
    
    for i in range(len(W[0])): 
        tmp = tools.multiplier_matrice_point(M,[W[0][i],W[1][i],W[2][i]])       
        newW[0].append(tmp[0]) 
        newW[1].append(tmp[1]) 
        newW[2].append(tmp[2])
    
    return newW