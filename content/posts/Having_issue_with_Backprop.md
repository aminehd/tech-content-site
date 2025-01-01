+++
title = "Having issue with understanding Backpropagation?"
date = "2024-12-30"

[taxonomies]
tags=["documentation"]

[extra]
repo_view = true
comment = true
+++



If you have ever found yourself struggling to understand backpropagation, follow my questions and take a deep breath :)

- 🌟 **Do you know the difference between the Total Derivative $ df/dt $ and the Partial Derivative $ \partial f/\partial t $?**  
   $ df/dt $ accounts for all the ways in which $ f $ changes as $ t $ changes, while $ \partial f/\partial t $ only considers the direct effect of $ t $ on $ f $. For functions of a single variable, $ df/dt $ and $ \partial f/\partial t $ are essentially the same. See below example and read more on [Math StackExchange](https://math.stackexchange.com/questions/2277214/the-difference-between-frac-dfdt-and-frac-partial-f-partial-t).

    For example for a function $ f(x(t), y(t), t) $:
  $$
   \frac{df}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt} + \frac{\partial f}{\partial t}
  $$
- 🔗 **Have you heard of the Chain Rule?**  Does chain rule apply for partial derivatives or total derivatives? 

- 📐 **Do you know how to move from simple derivatives to vectorized ones?**  
   Read about [Vectorized Derivatives](https://web.stanford.edu/class/cs224n/readings/gradient-notes.pdf). Pay close attention to the "Useful Identities" section.  
   For a matrix $ A $, vector $ x $, and scalar $ a $, we have the following identity, where $x = (x_1, ..., x_n) \in \mathbb{R}^n$ and $f(x) \in \mathbb{R}_m$:  
  $$
   \frac{\partial f}{\partial x} =
   \begin{bmatrix}
   \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
   \vdots & \ddots & \vdots \\
   \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
   \end{bmatrix}
  $$
    >Is $ \frac{\partial f}{\partial x} $ equal to $ \frac{df}{dx} $? 
    
    > What is the dimension of $ \frac{\partial f}{\partial x} $?

  $\frac{\partial f}{\partial x}$ is called the Jacobian matrix. Do you know Jacobian's matrix is a linear transformation in the space of functions? Wait what *Function Space*? 🤯

- 📚 **Have you read Andrej Karpathy's [Intuitive Understanding of Backpropagation](https://cs231n.github.io/optimization-2/#intro)?**  
   Have you tried to understand what he means by local gradients and backpropagation being a local process? What about staged backpropagation?

- 🧠 **Do you know cool tricks to calculate complex derivatives?**  
   For example, how do you calculate the derivative of the sigmoid function? Here it is (though I didn’t prove it—you can!):  
  $$
   \sigma(x) = \frac{1}{1 + e^{-x}}\\
   \frac{d\sigma}{dx} = \sigma(x) \cdot (1 - \sigma(x))
  $$

- 🧠 **Do you want to see 5 lines of code that summerizes it?**  No problem
```python
# Forward pass
x = gate1.forward(a)
y = gate2.forward(x)

# Backward pass
dL_dy = ... # gradient of loss w.r.t. final output
dL_dx = gate2.backward(dL_dy) # ∂L/∂x = (∂L/∂y) * (∂y/∂x)
dL_da = gate1.backward(dL_dx) # ∂L/∂a = (∂L/∂x) * (∂x/∂a)

```
