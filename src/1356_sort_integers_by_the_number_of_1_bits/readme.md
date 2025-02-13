## What Did I Learn?

### In this challenge I learned:

1. Create a function for first order the amount of numbers '1's in binaries, then the original number
```python
def custom_sort_key(num):
    bit_count = bin(num).count('1')
    return (bit_count, num)
```

2. Sort the input list using the custom comparison key function
```python
arr.sort(key=custom_sort_key)
```