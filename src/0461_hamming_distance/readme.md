## What Did I Learn?

### In this challenge I learned:

1. Discover the size of the largest binary number.
```python
max_len = max(len(bin(x)[2:]), len(bin(y)[2:]))
```

2. Format the numbers to have the same size by adding zeros to the left when necessary.
```python
bin1 = format(x, '0{}b'.format(max_len))
bin2 = format(y, '0{}b'.format(max_len))
```