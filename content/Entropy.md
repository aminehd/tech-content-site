+++
title = "Entropy and creativity"
date = "2025-01-19"

[taxonomies]
tags=["documentation"]

[extra]
repo_view = true
comment = true
+++

One of the definitions I have the least difficulty with is this one: Entropy is the amount of lack of knowledge in a system. In other words, the more a system gains entropy and becomes chaotic, the less knowledge an observer has about the system. Lack of knowledge means uncertainty, and uncertainty can be tied to the number of possibilities. So you can think about a probability distribution over the possibilities of the system. If there is only one possible state x, then the probability distribution is 1 for x and 0 for all other states. This is the most certain state and has the least entropy.

Entropy is commonly measured for thermodynamic systems. In this case, the number of particles and their energy is the most important factor about entropy because it determines the probability distributions over the possibilities. But we can also come up with a setup to define and measure entropy for information systems. Consider a sentence with a blank placeholder: "I am going to my home to feed my pet camels with ---". The more words you can fill in the blank, the more possibilities there are, so the more entropy the sentence has. Mathematically, this means entropy is a property of a probability distribution over all possible words that can go into the blank.
$$
P(w) = \textit{probability of word w going into the blank}
$$

Now think about a half-filled mathematical proof with a lot of blank spaces. Again, there are a lot of possibilities to complete the proof, and you can define the same probability distribution over the possibilities.
$$
P(p) = \textit{probability of proof p being the correct completion}
$$

Let's say you want to train a large language model (LLM) to fill in the blank. Let's say you have a machine learning model that tries to find the most likely answer, meaning it tries to minimize the cross entropy function. However, humans have a tendency to like more creative solutions. Can we somehow relate the creativity of a solution to the entropy? The first thing that comes to my mind is a more creative solution is a less likely solution. But is this true? Because in that case trying to minimize the cross-entropy function would be a bad idea.

But what if we have a data set full of creative answers and that is our reference distribution. Then can we say that a creative answer to the question is more likely to a less creative answer?


Prior probability VS likelihood:
To solve the apparent conflict, we can get a bit more exact about the given probability distribution and the likelihoods of data. In fact the distinction or prior probability and the likelihood can explain some qualities of creativity. Let's say we just have a complete blank sentence with 4 placeholders (-- -- -- --). Then all we need is a prior probability over all possible combinations of 4 words. 

Let say we start adding context to it. Like , "Hey, My uncle knew the secret of life and he said it can be said with 4 words.  -- -- -- --." Then we still have a prior probability of all possible combination of 4 words but now we have a posterior probability  after observing the data. The likelihood of the data is the probability of the data given the model. 

$$
P(w_1, w_2, w_3, w_4 | "\textit{Hey, My uncle knew the secret of the life and he said it can be said with 4 words}")
$$

In that you don't want to find the most likely sentence but you want to find the most likely sentence given the context. So maybe creativity does depend on the context. Maybe creativity actually needs some context. Maybe if you try to be creative without context, you are just being obnoxious. 
Can we say the farther the posterior probability is from the prior probability, the more surprise is there? and when we find a more surprising answer the more creative it is? What is it related to entropy? Can we say a more creative answer decreases the entropy of the system ever more than a less-creative, less surprising one?

