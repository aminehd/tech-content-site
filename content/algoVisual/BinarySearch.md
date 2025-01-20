+++
title = "Binary search as patitioning based on condtion change"
date = "2024-07-09"

[taxonomies]
tags=["documentation"]

[extra]
repo_view = true
comment = true
+++

# Binary Search: Beyond Finding Values - A Mental Model for Solving Problems
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1501892853/
## The Power of Mental Models

Most developers learn binary search as an algorithm to efficiently find a value in a sorted array. However, this mental model limits our understanding of binary search's true potential. There's a more powerful way to think about it:

> Binary search doesn't just find values - it finds the exact point where a boolean condition changes from False to True in a sorted sequence.

This shift in perspective transforms binary search from a simple lookup algorithm into a powerful tool for solving a wide range of problems.

## The Traditional vs. Powerful View

### Traditional View
- Binary search finds a specific value
- It works by repeatedly dividing the search space
- It returns the position of the target or indicates it's not found

### Powerful View
- Binary search finds a partition point in a monotonic sequence
- It identifies where a boolean condition transitions from False to True
- It can solve any problem that can be framed as finding such a transition

## Understanding Boundary Conditions

The key to this powerful view is the concept of a "boundary condition" - a predicate function that returns True/False and has a clear transition point. Let's look at a concrete example:

```python
# Array:     [1, 2, 2, 2, 3, 4]
# Target: 2

# For leftmost 2:
# Values:    [1, 2, 2, 2, 3, 4]
# Condition: [F, T, T, T, T, T]  (x >= 2)
#               ^ we want this position

# For rightmost 2:
# Values:    [1, 2, 2, 2, 3, 4]
# Condition: [F, F, F, F, T, T]  (x > 2)
#                     ^ we want this position
```

## The Abstract Binary Search

Here's how we can implement binary search to make this boundary condition concept explicit:

```python
def abstract_binary_search(nums, boundary_condition):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if boundary_condition(nums[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo
```
Here more abstract version:
```python
if left:
    # Finding leftmost: condition is "≥ target"
    boundary_condition = lambda x: x >= target
else:
    # Finding rightmost: condition is "> target"
    boundary_condition = lambda x: x > target
```
## Common Boundary Conditions and Their Uses

Here are some useful boundary conditions and what they find:

```python
# Find leftmost occurrence of target
lambda x: x >= target

# Find rightmost occurrence of target
lambda x: x > target

# Find first element greater than target
lambda x: x > target

# Find last element less than target
lambda x: x >= target

# Find square root (integer)
lambda x: x * x > target
```

## Practical Applications

This mental model lets us solve many problems elegantly:

1. **Finding Element Positions with Duplicates**
```python
def find_leftmost(nums, target):
    return abstract_binary_search(nums, lambda x: x >= target)

def find_rightmost(nums, target):
    return abstract_binary_search(nums, lambda x: x > target)

# Count occurrences
count = find_rightmost(nums, target) - find_leftmost(nums, target)
```

2. **Finding Insertion Points**
```python
def find_insertion_point(nums, target):
    return abstract_binary_search(nums, lambda x: x >= target)
```

3. **Finding Square Roots**
```python
def integer_sqrt(n):
    return abstract_binary_search(range(n+1), lambda x: x * x > n) - 1
```

## The Loop Invariant

The correctness of this approach relies on maintaining a crucial loop invariant:
- Everything before `lo` fails the condition (is False)
- Everything at or after `hi` satisfies the condition (is True)
- The answer must be at position `lo` when the loop terminates

## Why This Matters

Understanding binary search as a tool for finding boundary points rather than just values:
1. Makes the algorithm more versatile
2. Simplifies handling of edge cases
3. Makes it easier to adapt to new problems
4. Provides a framework for proving correctness

## Questions This View Answers

Once you understand binary search as finding a boundary condition, you can solve these types of questions elegantly:

### Array Problems
1. "Find the first/last position of element X in a sorted array with duplicates"
   - Boundary condition: `x >= target` or `x > target`

2. "Find the smallest element greater than X"
   - Boundary condition: `x > target`

3. "Find where to insert X to maintain sorted order"
   - Boundary condition: `x >= target`

4. "Find minimum element in a rotated sorted array"
   - Boundary condition: `x < array[0]` (first element smaller than original first element)

5. "Find peak element in mountain array"
   - Boundary condition: `x > x+1` (first decreasing element)

### Numeric Problems
6. "Calculate square root of N (floor value)"
   - Boundary condition: `x * x > N`

7. "Find smallest divisor greater than 1"
   - Boundary condition: `N % x == 0`

8. "Find smallest number with sum of digits > X"
   - Boundary condition: `sum_of_digits(n) > X`

### Matrix Problems
9. "Find median in row-wise sorted matrix"
   - Boundary condition: `count_elements_less_than(x) > total/2`

10. "Find kth smallest element in sorted matrix"
    - Boundary condition: `count_elements_less_than(x) >= k`

### Optimization Problems
11. "Find minimum capacity needed to ship packages within D days"
    - Boundary condition: `can_ship_with_capacity(x, D)`

12. "Find minimum time to complete all jobs with K workers"
    - Boundary condition: `can_complete_in_time(x, K)`

### String Problems
13. "Find smallest string that contains all strings as substring"
    - Boundary condition: `can_form_string_of_length(x)`

14. "Find longest common prefix"
    - Boundary condition: `is_prefix_for_all(x)`

### System Design Problems
15. "Find optimal server capacity"
    - Boundary condition: `can_handle_load(capacity)`

16. "Rate limiter threshold"
    - Boundary condition: `exceeds_rate_limit(requests_per_second)`

### Machine Learning Applications
17. "Find optimal learning rate"
    - Boundary condition: `convergence_rate(lr) > threshold`

18. "Hyperparameter tuning"
    - Boundary condition: `validation_score(param) > target`

## Real-World Applications

The boundary condition view makes binary search applicable to:
1. Database query optimization (finding optimal index positions)
2. Load balancer thresholds
3. Resource allocation in distributed systems
4. Image processing (finding threshold values)
5. Financial algorithms (finding optimal trading parameters)
6. Game development (difficulty scaling)
7. Network packet routing (finding optimal paths)
8. Machine learning model tuning

## Conclusion

The next time you encounter a problem that involves finding a position where some property changes, remember: binary search isn't just for finding values - it's for finding boundaries. This mental model will help you recognize and solve a much wider range of problems efficiently.

Remember the key insight: any problem that can be framed as finding the point where a boolean condition changes from False to True in a monotonic sequence can be solved using binary search.
