## What Did I Learn?

### In this challenge I learned:

1. Using `Counter ()` to tell how many times each element of the list is repeated
```python
c = Counter(nums)
```

2. Performing a for loop that goes through all the number and its quantity. We return the number that the quantity is = a n.
```python
next((num for num, quant in c.items() if quant == n), None)
```
`next ()` Pause in the first element that the loop finds, if you find none, returns None.