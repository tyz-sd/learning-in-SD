# notes-1

straight prob.:
$$
|S| = C_{10}^1 * (4^5 - 4) = 10200\\
P(S) = |S|/|\Omega| = 10220/2598960\\
$$
Event that a 5-card contains heart King:
$$
|S| = C_{51} ^ 4\\
P(S) = |S|/|\Omega| = 5/52
$$
split 52 cards into 5 cards and 47 cards. The probability equals to heart King lies in the 5 cards.

the informal way and formal way of defining independence:
$$
informal: P(F) = P(F|E) \Rightarrow asymmetric\\
formal: P(E\cap F) = P(E) \cdot P(F)\\
\therefore P(F|E) = P(F) \rightarrow  P(E|F) =P(E)\\
$$


convert probability to conditional probability: $ P(F|E )= \dfrac{P(E\cap F)}{P(E)}$

Three events:$P(E\cap F\cap G) = P(E) * P(F|E) * P(G|F\cap E)$

conclusion is similar for more events.



The birthday paradox: How many people does it take so two will likely share a birthday?
$$
P(S_2) = \frac{1}{365}\\
P(S_3) = \frac{1}{365^2} + \frac{1}{365}\cdot \frac{364}{365} \cdot 3 \approx \frac{3}{365}\\
$$
Q: What is the first n making $P(S_n) \geq \frac{1}{2} $

def the distinct event as $D_n$ : $D_n = S_n ^c$

def $N_i$ as the event of i-th birthday is new:
$$
P(D_n) = P(N_1\cap \cdots \cap N_n) = P(N_1) \cdot P(N_2|N_1) \cdots P(N_n|N_1 \cap \cdots \cap N_n)\\
= \prod _{i = 1}^{n-1} P(N_i | D_{n-1}) = 1 - \frac{i}{365}\\
\therefore P(D_i) \leq \prod_{i = 1} ^{n-1} e^{-\frac{i}{365}} = \exp(-\frac{1}{365} \sum _{i = 1} ^ {n-1} i) \leq exp(-\frac{n^2}{2\cdot 365}) \leq \frac{1}{2}\\
\therefore n \geq \sqrt{2\cdot 365\cdot \ln 2} \approx 22.494\\
\\
$$
Why roughly $\sqrt{365} $?
$$
P(S_2) = \frac{1}{365}\\
n\ people \Rightarrow \frac{n^2}{2} \ pairs\\
each\ pairs\ share\ the\ possibility\ of \ \frac{1}{365}\\
$$
What's the biggest paradox about the birthday paradox: That it's called a paradox.

total probability law: break into events ; Use chain rules for each ; combine probabilities
$$
F = (E\cap F) \cup (E^c \cap F)\\
P(F) = P(E\cap F) + P(E^c \cap F)\\
= P(E) \cdot P(F|E) + P(E^c) \cdot P(F|E^c)\\
$$
Three iphone factories produce separately 50%, 30%, 20% of iphone

Bayes' Rule: Given $P(F|E) , P(E) , P(F) $determines $P(E|F)$
$$
P(E|F) = \frac{P(E) \cdot P(F|E)}{P(F)}\\
P(F_1|D) = \frac{P(F_1)\cdot P(D|F_1)}{P(D)} = \frac{1}{3}\\
P(F_2|D) = \frac{1}{2}\\
P(F_3|D) = \frac{1}{6}\\
$$
conditional probabilities add to 1.

### expectation

when sample number becomes near to greater infinity, the event $X$ will appear $P(X) \cdot n$ times.

average:
$$
Average = \frac{\sum_x [P(x) \cdot n] \cdot x}{n} = \sum_x P(x)\cdot x = E(X)
$$
Expectation is not a random number, in fact it's a constant.
$$
x \in \N, p_i = P(x = i)\\
Ex = \sum_{i = 0}^ \infty ip_i = P(X\geq 1) + P(X\geq 2) + \cdots\\\
$$
Pick Queen of hearts:

Queen location is uniformly over $1,\cdots, 52$
$$
EX = \frac{1+52}{2} = 26.5\\
$$

### expectations of modified variables

$$
E(g(X)) =  \sum_{x} g(X) \cdot p(X)\\
e.g: E(x) = \sum_{x} xp(x)\rightarrow E(2x) = \sum_{x} 2xp(x) = 2E(x)\\
$$

Joint distribution: a simple extension of pmf, called joint pmf

* linearity of expectations

$$
E(aX + bY + c) = aE(X) + bE(Y) + c
$$

indicator variables	
$$
d = 1,\cdots, 365;I_d = \begin{cases}
1,&born\ on\ day\ d\\
0,&no\ student\ born\ on\ day\ d\\
\end{cases}\\
for\ n\ students: P(I_d = 0) = (\frac{364}{365}) ^n\\
distinct\ birthdays: D = \sum_{d} I_d = \sum_{d = 1} ^{365} I_d = 365\cdot (1-(\frac{364}{365})^n)\\
$$
bernoulli distribution:

two values with probability of p and 1-p

Variance: Expected squared difference between X and its mean
$$
V(X) = E[(X-\mu) ^2] = E(X-\mu)^2\\
\sigma_x = +\sqrt{V(X)}\\
$$
alternative variance expression
$$
V(X) = E(X-\mu)^2\\
=E(X^2) - 2(\mu X) + \mu^2\\
=E(X^2) - E(X)^2
$$

$$
cov(X,Y) = E[(x - \mu_x)(y-\mu_y)]

$$













## exercise 1

What is the probability that a random integer between 1 and 100, inclusive of both, contains the digit 7, e.g. 7,27,77?

A: from 7 to 97, there are 10, from 70 to 79, there are 10, exclude 77, total 19

