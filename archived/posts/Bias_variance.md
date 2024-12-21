Understanding statistical definiton of Bias and Variance
 
 ### Why Bias and Variance matter?
In practical machine learn,   we would want to know if trained models are overfitting or underfitting.
Overfitting is associated with high Variance and underfitting is associated with high Bias.
But the use of term variance is not exactly the same as the statistical variance.

### Why overfitting is associated with high Variance?
Overfitting means that if we pick a different training set, we would get a different model. That is roughly what we mean by Variance. 
In more exat terms the Variance is the Variance of the predictions for y_0 = f(x_0).
But Variance has a very specific definition in statistics. How would that relate to the above definition?

### Statistic definition of variance
In statistics variance is the average of the squared differences from the Mean of a set of number.
This brings us to our next question. Variance over which set? Answer is over set of all possible training sets. Yeah sets of sets sounds too nerdy to me as well.
To make this more concrete I use a 1D input feature X and sampled 1000 Y's for that. 

On the left side you you see the whole data set X in Grey and the training set we have chosen in blue. 
On the right side you see the line that would be trained on the training set.
The red dots is the test datapoint. 
Now you might ask why we might smaple different training sets. Why don't we just use the whole data set?
The answer is that we don't know the whole data set. The wholde data set is the population and we can only have some assuption about it. For example we can assume the popluations is normally distributed.
Doing this we can have a formula for Bias and Variance.
$$
E[(f(x_0) - y_0)^2] = Bias^2 + Variance + Noise
$$
have you ever wondered why overfitting is associated with high Variance and underfitting is associated with high Bias?