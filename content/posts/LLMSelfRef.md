+++
title = "LLMs and Gödelian Self-Reference"
date = "2025-03-19"

[taxonomies]
tags=["documentation"]

[extra]
repo_view = true
comment = true
+++

# LLMs and Gödelian Self-Reference

I have been recently reading "I Am a Strange Loop" by Douglas Hofstadter. The book explains Gödel's incompleteness theorem and how it relates to human consciousness.

---

## Gödel's Self-Referential System

For the first part, it explains how Gödel created a system where mathematical statements could refer to themselves through an encoding.

In a very high level:

> 🔄 **Step 1:** He created a mapping from logical statements to numbers.
> 
> 🔄 **Step 2:** Then he created meta-logical statements of the form "The number associated with this statement has such property". That is because the logical framework was able to talk about properties of numbers.
> 
> 🔄 **Step 3:** He used a technique to make such a meta-statement that talks about the Gödel number of the statement itself.
> 
> 🔄 **Step 4:** Lastly, he uses the mapping to carry out a level shift. What is a level shift?
> 
> 🔄 **Step 5:** The level shift happens when whatever is true about the Gödel number is also true about the statement that number is encoding. So the meta-statement we started with is talking about itself through a level shift.

---

## LLMs and Self-Reference

Now looking at LLMs, there are some similarities:

> 🤖 LLMs can learn meta-statements. For example, we can teach LLMs to talk about the properties of the network structure and the weights of a certain class of LLMs that they themselves belong to.
> 
> 🤖 Then they will be talking about the lower level entities that are the weights and the code that makes themselves. So they can talk about themselves through a level shift. _(Weights → low level, Sentences that are output of LLM → high level)_
> 
> 🤖 We can add an agent to the output of LLM. This agent can do 2 types of things:
> 
> 1. It can try to update the weights based on what it learned about its own weights
> 2. It can query the LLM about its self-knowledge, and feed the answer back to the LLM.

---

## The Strange Loop Connection

This can be somewhat similar to Hofstadter's idea of human consciousness: **the self-referential loop of the brain**.
