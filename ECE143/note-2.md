# note-2

equation for a line:
$$
Weight = m_1 \times Height + m_2\times age + b\\
y = m_1x_1 + m_2x_2 +b\\
w = [height, age, 1] \cdot [m_1, m_2, b]\\
$$
separately managed the knowns and unknowns:
$$
y = x \cdot \theta\\	
$$
linear regression:  
$$
X\theta = y\\
$$
$\theta$ represent all unknown features
$$
X^{-1} X \theta = X^{-1} Y
$$
but X is not a square matrix.
$$
X^TX \theta = X^T y\\
(X^TX)^{-1}(X^TX)\theta = (X^TX)^{-1} X^T y\\
\theta = (X^TX)^{-1} X^T y\\
$$
E1: How do preferences toward certain age varies?

model : 
$$
rating = \theta_0 + \theta_1 \times age
$$


X must conclude a line of 1 because there might be constants in the equation.

what if the assumption of same diff between two features are not valid:

eg: male, female, other, not specified

feature: [1,0,0] for female ; [0,1,0] for other ; [0,0,1] for not specified

equivalent to: 
$$
(\theta_1, \theta_2, \theta_3,\theta_4) \cdot (1, feature)\\
$$
called one hot coding

Other coding methods:

male = [0, 1] female = [1,0] -> there are redundant dimensions **don't use redundant dimensions on the feature level**



what about model with time: 

 using one hot encoding



distinguish good model from bad one:

regression diagnostics 







#### MSE

mean square error:
$$
\frac{1}{N} ||y-X\theta||_2^2\\
= \dfrac{1}{N} \sum_{i=1}^n(y_i - X_i\cdot \theta)^2\\
||x||_2^2 = \sum_{ i = 1}^n x_i^2
$$

* why we take the mean square error:

eliminate small error and enlarge the big error. 

* why square not cube?

$$
d_i = y_i - X_i \theta\\
$$

the distribution of di determines the small errors are common but large errors are unlikely happening. $N(0, \theta)$
$$
P_{\theta} (y_i | x_i) = \prod_i\frac{1}{\sqrt{2\pi } \sigma} e^{-\frac{y_i - x_i\theta}{\sigma^2}}\\
\max_{\theta} P_{\theta}(y|x) = \sum_i -(y_i - x_i \cdot \theta) ^2 = \min_{\theta} \sum_{i} (y_i - x_i \cdot \theta)\\
mean: \overline{y} = \frac{1}{N} \sum y_i\\
variance: var(Y) = \frac{1}{N} \sum(y_i - \overline{y})^2\\
MSE: MSE_{\theta}(y|X) = \frac{1}{N} \sum_i (y_i - x_i \cdot \theta)^2\\
FVU(f) = \frac{MSE(f)}{Var(y)}\\
FVU(f) = 1 \rightarrow Trivial \ predictor\\
FYU(f) = 0 \rightarrow perfect \ perdictor\\
R^2 = 1-FVU(f)\\
$$


overfitting:

model performs well on training data but doesnt generalize.

Occam's razor: Among all competing hypotheses, the one with the fewest assumptions should be selected.	



A1: simple model is one where theta has few non-zero parameters

* low$\sum_{i} |\theta_i|$, small L1norm

A2: a simple model is on where theta is almost uniform

* low$\sum_{i} |\theta_i^2|$, small L2 norm	

we want models works well and not too complex
$$
\arg\min_{\theta} = \frac{1}{N} || y - X\theta||_2^2 + \lambda ||\theta||_2^2\\
$$
the model before will have the min MSE but not the best

#### optimizing the regularized model

using gradient descent to solve the function above

1. initialize $\theta$ at random first

2. wile not converged:
   $$
   \theta := \theta - \alpha f'(\theta)\\
   f(\theta) =\frac{1}{N} || y - X\theta||_2^2 + \lambda ||\theta||_2^2\\
   \frac{\partial f}{\partial \theta_k} = \frac{1}{N} \sum_i 2x_ik(y_i - x_i\theta) + 2\lambda \theta_k\\
   $$

how much should we trade-off accuracy versus complexity

A1: one with the lowest training error : lambda will be zero: not good

A2: one with the lowest test error: cheating, not good

S: validation set is constructed to 'tune' the model's parameters.

* Training set: optimize the model's parameters
* Test set: report how well we expect the model to perform on unseen data
* Validation set: used to tune any model parameters that are not directly optimized.



### classification

* explore techniques for classification, simple solutions and see why they fail

$$
previouly\ :\\
f(data) \rightarrow lables\\
$$

linear regression in order to learn linear relationships btw features and parameters to predict real-valued outputs.

gradient descent for model optimization:

1. initialize $\theta$ at random
2. $\theta' = \theta - \alpha f'(\theta)$

regularization pipeline

validation set is constructed to compute $\theta$

#### naive bayes

associate a probability with a label and its negation
$$
P(label|data)\\
P(\ne label | data)\\
$$
naive bayes assumes that the features are conditionally independent given the label
$$
P(label|features) = \frac{p(label)p(features|label)}{p(features)}\\
p(label|features) = \frac{p(label)\prod_i p(feature_i|label)}{p(features)}\\
$$
then we can give up the probability of features cause we only have to compare with is bigger.
double conunting:
$$
length = \theta_0 + \theta_1 [wizatds]\\
length = \theta_0  + \theta_2 [eixstfd]\\
$$

#### logistic regression classifier

how to design classifiers using logistic regression.

convert a real-valued expression into a probability
$$
sigmoid\ function :\sigma(t) = \frac{1}{1+e^{-t}}\\
P_{\theta}(y_i =  1| x_i) = \dfrac{1}{1+e^{X_i\theta}}\\
$$
training: $x_i\theta$ should be maximized when y_i is positive and minimized when y_i is negaative.
$$
\arg\max_{\theta} \prod_{y_i = 1} P_{\theta}(y_i = 1|x_i)\prod_{y_i = 0} (1-p_{\theta} (y_i = 0 | x_i))\\
$$
optimize method: 

using gradient ascent::	
$$
l_{\theta}(y|x) \sum_{y_i = 1} \log \frac{1}{1 + e^{-x_i\theta}} +  \sum_{y_i = 0} \log \frac{e^{-x_i\theta}}{1 + e^{-x_i\theta}} - \lambda \sum_{k} \theta_k^2\\
\frac{\partial l}{\partial \theta_k} = 
$$

#### SVM

















## HW1

1, how to transform the dimension of a np array:

`np.resize(a, size) ; np.reshape(size)`

2, how to output the dimension of a np array:

`np.shape # the shape`

`np.size # the size`



2 2 2 3 3 3 3 3 4 4