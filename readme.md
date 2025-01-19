# Bayesian Network Analysis Report

## Introduction
This report presents an in-depth analysis of a Bayesian network consisting of 5 variables and their probabilistic relationships.

## Network Structure
![Bayesian Network](bayesian_network.png)

The network consists of:
- 5 variables (nodes): S, D, R, G, L
- 4 directed edges with conditional probabilities: S→R, S→G, D→G, G→L

## Probability Tables
To be more efficient, we define the probability tables in numpy array, with the following API

```python
P(S=s0) = P_S[0]
P(D=d1) = P_D[1]
P(R=r1|S=s0) = P_R_S[1,0]
P(G|S=s0,D=d1) = P_G_SD[0,1] = P_G_SD[0,1,:]
P(L|G=g0) = P_L_G[:,0]
```

## Key Probability Calculations

### 1. Marginal Probability P(G)

We have the following formula deriving from law of total probability and the network structure that we will abuse to compute all the probabilities :
$$P(S,D,R,G,L) = P(S)P(D)P(R|S)P(G|S,D)P(L|G)$$

For example P(G) can be computed like that by marginalising S and D

$$P(G) = \sum_{s,d} P(S=s)P(D=d)P(G|S=s,D=d)$$

### 2. Conditional Independence

One interesting finding is that R and D are conditionally independent given S:

$$P(R|D,S) = P(R|S)$$

### 3. Do-calculus Analysis
When analyzing interventions like $P(R|do(G=g_2))$, we found that:

$$P(R|do(G=g_2)) = P(R)$$

This shows that forcing G to a specific value breaks its causal relationship with S.

## Key Insights

1. **Independence Properties**:
   - R and D are marginally independent
   - S and D are independent
   - L is conditionally independent of all other variables given G

2. **Causal Effects**:
   - Interventional probabilities often differ from observational ones
   - The do-operator reveals true causal relationships

## Skills Acquired

1. **Probabilistic Reasoning**:
   - Mastery of joint probability decomposition
   - Understanding of conditional independence

2. **Bayesian Network Analysis**:
   - Ability to compute marginal and conditional probabilities
   - Understanding of d-separation and causal relationships

3. **Programming Skills**:
   - Implementation of probabilistic calculations in Python
   - Use of NumPy for probability computations

4. **Causal Inference**:
   - Understanding of do-calculus
   - Distinction between observational and interventional probabilities

## Conclusion
This analysis demonstrates the power of Bayesian networks in modeling complex probabilistic relationships and causal effects. The implementation successfully validates theoretical probabilities through computational methods.