# Bayesian Network Analysis Report

## Introduction
This report presents an in-depth analysis of a Bayesian network consisting of 5 variables and their probabilistic relationships.

## Network Structure
![Bayesian Network](bayesian_network.png)

The network consists of:
- 5 variables (nodes): S, D, R, G, L
- 4 directed edges with conditional probabilities: S→R, S→G, D→G, G→L

## Probability Tables
The network is defined by the following probability tables:

```python
P_S = [0.2, 0.8]              # P(S)
P_D = [0.9, 0.1]              # P(D)
P_R_S = [[0.9, 0.2],         # P(R|S)
         [0.1, 0.8]]
```

## Key Probability Calculations

### 1. Marginal Probability P(G)
The marginal probability P(G) can be computed using the law of total probability:

$$P(G) = \sum_{s,d} P(G|S=s,D=d)P(S=s)P(D=d)$$

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
   - Efficient use of NumPy for probability computations

4. **Causal Inference**:
   - Understanding of do-calculus
   - Distinction between observational and interventional probabilities

## Conclusion
This analysis demonstrates the power of Bayesian networks in modeling complex probabilistic relationships and causal effects. The implementation successfully validates theoretical probabilities through computational methods.