def SommeList(L1: list[float],L2: list[float]):
    L3: list = []
    for i in range(len(L1)):
        L3.append(L1[i]+L2[i])
    return L3


def Derive(v_2:list[float],a_1:list[float],h:float):
    return SommeList(a_1 * h, v_2) 

def Translation(m:float,F:list[list[list[float]]],G:list[list[list[float]]],vG:list[float,float,float],h:float): 

    #Calcul somme des forces
    sommeAcc : list[float] = [0,0,0]
    for i in range(len(F)):
        sommeAcc = SommeList(sommeAcc,F[i][0]) 
    sommeForce: list[float]  = sommeAcc * m

    #Calcul nouvelle vitesse
    new_vG : list[float] = Derive(vG,sommeForce,h)

    #Calcul nouvelle position
    # for i in range(len(G)):
    #     for j in range(len(G[i])):
    #         for k in range(len(G[i])):
    #             G[i][j][k] = Derive(G[i][j][k],new_vG,h)
    for k in range(len(G[i])):
        G[20][0][k] = Derive(G[0][0][k],new_vG,h)
    
    new_G :list[list[list[float]]] = G
    return new_vG, new_G
