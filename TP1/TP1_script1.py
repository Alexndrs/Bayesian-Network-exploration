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
# P(G|S=s0,D=d1) = P_G_SD[0,1,:]
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
# b) P(G|R=r1)
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
# c) P(G|R=r0) = P(G,R=r0) / P(R=r0) = P(G,R=r0) / (1 - P(R=r1))
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
# d) P(G|R=r1,S=s0)

