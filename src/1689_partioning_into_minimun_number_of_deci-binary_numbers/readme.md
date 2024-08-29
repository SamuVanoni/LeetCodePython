## What Did I Learn?

### In this challenge I learned a function that does what I wanted to do faster:

1. max()
```python
return int(max(n))
```
This function takes the biggest value from a set of values

2. How would I do it without the function
```python
varMax = 0
for i in range(len(n)):
    if n[i] > varMax:
        varMax = n[i]
return int(varMax)
```
