## What Did I Learn?

### In this challenge I learned:

1. How to turn a base number 10 to another base
```python
while (n // k) > 0:
    baseK += str(n % k)
    n = n // k
baseK += str(n)
```

2. Remembering how to sum up the numbers in a string
```python
return sum(int(d) for d in baseK)
```