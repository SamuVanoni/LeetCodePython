## What Did I Learn?

### In this challenge I learned:

1. We turn the number into string to get each character through a for loop
```python
for char in str(i):
```

2. If one of Char = 0 or if this element does not divide the integer = break
```python
if int(char) == 0 or i % int(char) != 0:
    break
```