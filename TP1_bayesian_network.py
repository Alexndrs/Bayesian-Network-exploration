import numpy as np

# Bayesian network : 
#   - 5 variables (nodes) : S, D, R, G, L
#   - 4 relations (edges) with conditional probabilities : S->R, S->G, D->G, G->L

# Probabilities tables

# [P(S=S0), P(S=S1)]
P_S = np.array([0.2, 0.8])

# [P(D=D0), P(D=D1)]
P_D = np.array([0.9, 0.1]) 

# [P(R=R0|S=S0), P(R=R0|S=S1),
# P(R=R1|S=S0), P(R=R1|S=S1)]
P_R_S = np.array([[0.9, 0.2], [0.1, 0.8]]) 

# [P(G=G0|S=S0,D=D0), P(G=G1|S=S0,D=D0), P(G=G2|S=S0,D=D0),
# P(G=G0|S=S0,D=D1), P(G=G1|S=S0,D=D1), P(G=G2|S=S0,D=D1), 
# P(G=G0|S=S1,D=D0), P(G=G1|S=S1,D=D0), P(G=G2|S=S1,D=D0), 
# P(G=G0|S=S1,D=D1), P(G=G1|S=S1,D=D1), P(G=G2|S=S1,D=D1)]
P_G_SD = np.array([[[0.5, 0.3, 0.2], [0.9, 0.08, 0.02]], [[0.1, 0.2, 0.7], [0.3, 0.4, 0.3]]])

# [P(L=L0|G=G0), P(L=L0|G=G1), P(L=L0|G=G2),
# P(L=L1|G=G0), P(L=L1|G=G1), P(L=L1|G=G2)]
P_L_G = np.array([[0.9,0.6,0.01], [0.1,0.4,0.99]]) 

#API for proba : 
# P(S=s0) = P_S[0]
# P(D=d1) = P_D[1]
# P(R=r1|S=s0) = P_R_S[1,0]
# P(G|S=s0,D=d1) = P_G_SD[0,1] = P_G_SD[0,1,:]

# P(L|G=g0) = P_L_G[:,0]


# Question 1 :

# We have generally P(S,D,R,G,L) = P(S).P(D).P(R|S).P(G|S,D).P(L|G), we will abuse of this formula to compute all the probabilities
# first we test it on the first Proba

#___________________________________________________________________________________________________________________________
print("\n\n----- a) P(G) -----\n")
# a) P(G)


# First and usual method if we want to calculate probability by hand is :
# P(G) = P(G|S,D).P(S,D) = P(G|S,D).P(S).P(D) (independence between S and D) = sum_{s,d} P(G|S=s,D=d).P(S=s).P(D=d)
def compute_P_G():
    P_G = np.zeros(3)
    for s in range(2):
        for d in range(2):
            P_G += P_G_SD[s,d] * P_S[s] * P_D[d]
    return P_G

# Using the general formula we get the same result
# P(G) = \sum_{s,d,r,l} P(S=s).P(D=d).P(R=r|S=s).P(G|S=s,D=d).P(L=l|G)
def compute_P_G_other_way():
    P_G = np.zeros(3)
    for s in range(2):
        for d in range(2):
            for r in range(2):
                for l in range(2):
                    P_G += P_S[s] * P_D[d] * P_R_S[r,s] * P_G_SD[s,d] * P_L_G[l]
    return P_G

# And we can even remove L from the formula since it is not a parent of G
# P(G) = \sum_{s,d,r} P(S=s).P(D=d).P(R=r|S=s).P(G|S=s,D=d)
def compute_P_G_other_other_way():
    P_G = np.zeros(3)
    for s in range(2):
        for d in range(2):
            for r in range(2):
                    P_G += P_S[s] * P_D[d] * P_R_S[r,s] * P_G_SD[s,d]
    return P_G
P_G = compute_P_G()
P_G_ = compute_P_G_other_way()
P_G__ = compute_P_G_other_other_way()
print("first method:\n\tP(G) = P(G|S,D).P(S,D) = P(G|S,D).P(S).P(D) (independence between S and D) = sum_{s,d} P(G|S=s,D=d).P(S=s).P(D=d)\n\tP(G) = ", P_G)
print("second method:\n\t P(G) = \sum_{s,d,r,l} P(S=s).P(D=d).P(R=r|S=s).P(G|S=s,D=d).P(L=l|G)\n\tP(G) = ", P_G_)
print("third method:\n\tP(G) = \sum_{s,d,r} P(S=s).P(D=d).P(R=r|S=s).P(G|S=s,D=d)\n\tP(G) = ", P_G__)
print("\n|We can see the differents methods give the same result,\n|for the following we will proceed like in the third method,\n|using the general formula and removing unnecessary variables")



#___________________________________________________________________________________________________________________________
print("\n\n----- b) P(G|R=r1) -----\n")
#    P(G|R=r1) = P(G,R=r1) / P(R=r1)
#    P(G,R=r1) = \sum_{s,d} P(S=s).P(D=d).P(R=r1|S=s).P(G|S=s,D=d)
#    P(R=r1) = \sum_s P(S=s).P(R=r1|S=s)

def compute_P_R1():
    P_R1 = 0
    for s in range(2):
        P_R1 += P_S[s] * P_R_S[1,s]
    return P_R1
P_R1 = compute_P_R1()

def compute_P_G_and_R1():
    P_G_and_R1 = np.zeros(3)
    for s in range(2):
        for d in range(2):
                P_G_and_R1 += P_S[s] * P_D[d] * P_R_S[1,s] * P_G_SD[s,d]
    return P_G_and_R1
P_G_and_R1 = compute_P_G_and_R1()
print("P(G|R=r1) = ", P_G_and_R1 / P_R1)



#___________________________________________________________________________________________________________________________
print("\n\n----- c) P(G|R=r0) -----\n")
#   P(G|R=r0) = P(G,R=r0) / P(R=r0) = P(G,R=r0) / (1 - P(R=r1))
def compute_P_G_and_R0():
    P_G_and_R0 = np.zeros(3)
    for s in range(2):
        for d in range(2):
                P_G_and_R0 += P_S[s] * P_D[d] * P_R_S[0,s] * P_G_SD[s,d]
    return P_G_and_R0
P_G_and_R0 = compute_P_G_and_R0()

print("P(G|R=r0) = ", P_G_and_R0 / (1-P_R1))



#___________________________________________________________________________________________________________________________
print("\n\n----- d) P(G|R=r1,S=s0) -----\n")
#   P(G|R=r1,S=s0) = P(G,R=r1,S=s0) / P(R=r1,S=s0) 
#   P(G,R=r1,S=s0) = \sum_d P(S=s0).P(D=d).P(R=r1|S=s0).P(G|S=s0,D=d)
#   P(R=r1,S=s0) = P(S=s0).P(R=r1|S=s0)

def compute_P_R1_and_S0():
    P_R1_and_S0 = P_S[0] * P_R_S[1,0]
    return P_R1_and_S0

def compute_P_G_and_and_R1_and_S0():
    P_G_and_R1_and_S0 = np.zeros(3)
    for d in range(2):
        P_G_and_R1_and_S0 += P_S[0] * P_D[d] * P_R_S[1,0] * P_G_SD[0,d]
    return P_G_and_R1_and_S0

P_R1_and_S0 = compute_P_R1_and_S0()
P_G_and_and_R1_and_S0 = compute_P_G_and_and_R1_and_S0()
print("P(G|R=r1,S=s0) = ", P_G_and_and_R1_and_S0 / P_R1_and_S0)


#___________________________________________________________________________________________________________________________
print("\n\n----- e) P(G|R=r0,S=s0) -----\n")
#   P(G|R=r0,S=s0) = P(G,R=r0,S=s0) / P(R=r0,S=s0) 
#   P(G,R=r0,S=s0) = \sum_d P(S=s0).P(D=d).P(R=r0|S=s0).P(G|S=s0,D=d)
#   P(R=r0,S=s0) = P(S=s0).P(R=r0|S=s0)

def compute_P_R0_and_S0():
    P_R0_and_S0 = P_S[0] * P_R_S[0,0]
    return P_R0_and_S0

def compute_P_G_and_and_R0_and_S0():
    P_G_and_R0_and_S0 = np.zeros(3)
    for d in range(2):
        P_G_and_R0_and_S0 += P_S[0] * P_D[d] * P_R_S[0,0] * P_G_SD[0,d]
    return P_G_and_R0_and_S0

P_R0_and_S0 = compute_P_R0_and_S0()
P_G_and_and_R0_and_S0 = compute_P_G_and_and_R0_and_S0()
print("P(G|R=r0,S=s0) = ", P_G_and_and_R0_and_S0 / P_R0_and_S0)
print("On aurait pu prévoir qu'on obient le même résultat pour R0 et R1, car la variable G conditionnées à S=0 est indépendante de R.")


#___________________________________________________________________________________________________________________________
print("\n\n----- f) P(R|D=d1) -----\n")
# On peut directement dire que P(R|D=d1) = P(R) car R est indépendant de D, on fait quand même le calcule pour le démontrer
# P(R|D=d1) = \sum_s P(R,S=s|D=d1) = sum_s P(R|S=s & D=d1).P(S=s|D=d1) = \sum_s P(R|S=s).P(S=s) = P(R) (car R est indépendant de D selon S fixé et S est indépendant de D)
# P(R|D=d1) = P(R) = [P(R=R0), P(R=R1)] = [1-P_R1, P_R1]


P_R1 = compute_P_R1()
P_R = np.array([1-P_R1, P_R1])
print("P(R|D=d1) = P(R) = ", P_R)


#___________________________________________________________________________________________________________________________
print("\n\n----- g) P(R|D=d0) -----\n")
print("P(R|D=d0) = P(R) = ", P_R)



#___________________________________________________________________________________________________________________________
print("\n\n----- h) P(R|D=d1,G=g2) -----\n")
# P(R|D=d1,G=g2) = P(R,D=d1,G=g2) / P(D=d1,G=g2)
# P(R,D=d1,G=g2) = \sum_s P(S=s).P(D=d1).P(R|S=s).P(G=g2|S=s,D=d1)
# P(D=d1,G=g2) = \sum_s P(S=s).P(D=d1).P(G=g2|S=s,D=d1)

def compute_P_R_and_D1_and_G2():
    P_R_and_D1_and_G2 = np.zeros(2)
    for s in range(2):
        P_R_and_D1_and_G2 += P_S[s] * P_D[1] * P_R_S[:,s] * P_G_SD[s,1,2]
    return P_R_and_D1_and_G2

def compute_P_D1_and_G2():
    P_D1_and_G2 = 0
    for s in range(2):
        P_D1_and_G2 += P_S[s] * P_D[1] * P_G_SD[s,1,2]
    return P_D1_and_G2

P_R_and_D1_and_G2 = compute_P_R_and_D1_and_G2()
P_D1_and_G2 = compute_P_D1_and_G2()
print("P(R|D=d1,G=g2) = ", P_R_and_D1_and_G2 / P_D1_and_G2)

#___________________________________________________________________________________________________________________________
print("\n\n----- i) P(R|D=d0,G=g2) -----\n")

def compute_P_R_and_D0_and_G2():
    P_R_and_D0_and_G2 = np.zeros(2)
    for s in range(2):
        P_R_and_D0_and_G2 += P_S[s] * P_D[0] * P_R_S[:,s] * P_G_SD[s,0,2]
    return P_R_and_D0_and_G2

def compute_P_D0_and_G2():
    P_D0_and_G2 = 0
    for s in range(2):
        P_D0_and_G2 += P_S[s] * P_D[0] * P_G_SD[s,0,2]
    return P_D0_and_G2

P_R_and_D0_and_G2 = compute_P_R_and_D0_and_G2()
P_D0_and_G2 = compute_P_D0_and_G2()
print("P(R|D=d0,G=g2) = ", P_R_and_D0_and_G2 / P_D0_and_G2)


#___________________________________________________________________________________________________________________________
print("\n\n----- j) P(R|D=d1,L=l1) -----\n")
# P(R|D=d1,L=l1) = P(R,D=d1,L=l1) / P(D=d1,L=l1)
# P(R,D=d1,L=l1) = \sum_{s,g} P(S=s).P(D=d1).P(R|S=s).P(G=g|S=s,D=d1).P(L=l1|G=g)
# P(D=d1,L=l1) = \sum_{s,g} P(S=s).P(D=d1).P(G=g|S=s,D=d1).P(L=l1|G=g)

def compute_P_R_and_D1_and_L1():
    P_R_and_D1_and_L1 = np.zeros(2)
    for s in range(2):
        for g in range(3):
            P_R_and_D1_and_L1 += P_S[s] * P_D[1] * P_R_S[:,s] * P_G_SD[s,1,g] * P_L_G[1,g]
    return P_R_and_D1_and_L1

def compute_P_D1_and_L1():
    P_D1_and_L1 = 0
    for s in range(2):
        for g in range(3):
            P_D1_and_L1 += P_S[s] * P_D[1] * P_G_SD[s,1,g] * P_L_G[1,g]
    return P_D1_and_L1

P_R_and_D1_and_L1 = compute_P_R_and_D1_and_L1()
P_D1_and_L1 = compute_P_D1_and_L1()
print("P(R|D=d1,L=l1) = ", P_R_and_D1_and_L1 / P_D1_and_L1)


#___________________________________________________________________________________________________________________________
print("\n\n----- k) P(R|D=d0,L=l1) -----\n")

def compute_P_R_and_D0_and_L1():
    P_R_and_D0_and_L1 = np.zeros(2)
    for s in range(2):
        for g in range(3):
            P_R_and_D0_and_L1 += P_S[s] * P_D[0] * P_R_S[:,s] * P_G_SD[s,0,g] * P_L_G[1,g]
    return P_R_and_D0_and_L1

def compute_P_D0_and_L1():
    P_D0_and_L1 = 0
    for s in range(2):
        for g in range(3):
            P_D0_and_L1 += P_S[s] * P_D[0] * P_G_SD[s,0,g] * P_L_G[1,g]
    return P_D0_and_L1

P_R_and_D0_and_L1 = compute_P_R_and_D0_and_L1()
P_D0_and_L1 = compute_P_D0_and_L1()
print("P(R|D=d0,L=l1) = ", P_R_and_D0_and_L1 / P_D0_and_L1)



#___________________________________________________________________________________________________________________________
print("\n\n----- l) P(R|do(G=g2)) -----\n")
#   P(R|do(G=g2)) = P(R) car R est si nous forçons la valeur de G celle ci n'est plus causée par S et donc est indépendante avec R

print("P(R|do(G=g2)) = P(R) = ", P_R)


#___________________________________________________________________________________________________________________________
print("\n\n----- m) P(R|G=g2) -----\n")
#   P(R|G=g2) = \sum_s P(R,S=s|G=g2) = \sum_s P(S=s|G=g2).P(R|S=s,G=g2) = \sum_s P(S=s|G=g2).P(R|S=s)
#   P(S=s|G=g2) = P(G=g2|S=s).P(S=s) / P(G=g2) = \sum_d P(G=g2|S=s,D=d).P(D=d).P(S=s) / P(G=g2)

def compute_P_S_G2():
    P_S_G2 = np.zeros(2)
    for d in range(2):
        P_S_G2 += P_G_SD[:,d,2] * P_D[d] * P_S[:]
    return P_S_G2 / P_G[2]
P_S_G2 = compute_P_S_G2()

def compute_R_G2():
    P_R_G2 = np.zeros(2)
    for s in range(2):
        P_R_G2 += P_S_G2[s] * P_R_S[:,s]
    return P_R_G2
P_R_G2 = compute_R_G2()
print("P(R|G=g2) = ", P_R_G2)


#___________________________________________________________________________________________________________________________
print("\n\n----- n) P(R) -----\n")
P_R1 = compute_P_R1()
P_R = np.array([1-P_R1, P_R1])
print("P(R) = ", P_R)



#___________________________________________________________________________________________________________________________
print("\n\n----- o) P(G|do(L=l1)) -----\n")
#   Le fait de forcer L à 1 ne change pas les probabilités de G,
#   P(G|do(L=l1)) = \sum_{s,d} P(G,S=s,D=d|do(L=l1)) = \sum_{s,d} P(G,S=s,D=d) (independance)
#                 = \sum_{s,d} P(G|S=s,D=d).P(S=s).P(D=d)
#                 = P(G)
print("P(G|do(L=l1)) = P(G) = ", P_G)



#___________________________________________________________________________________________________________________________
print("\n\n----- p) P(G=g1|L=l1) -----\n")
#   P(G=g1|L=l1) = P(L=l1|G=g1).P(G=g1) / P(L=l1)
#   P(L=l1) = \sum_{g} P(L=l1|G=g).P(G=g)

def compute_P_L1():
    P_L1 = 0
    for g in range(3):
        P_L1 += P_L_G[1,g]*P_G[g]
    return P_L1
P_L1 = compute_P_L1()

def compute_P_G1_L1():
    P_G1_L1 = P_L_G[1,1]*P_G[1] / P_L1
    return P_G1_L1
P_G1_L1 = compute_P_G1_L1()

print("P(G=g1|L=l1) = ", P_G1_L1)