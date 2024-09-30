## What Did I Learn?

### In this challenge I learned more about logic:

1. If string = 'aceg' the white colors will be in numbers that are multiples of two
```python
s="aceg"
if coordinates[0] in s:
    return int(coordinates[1]) % 2 == 0
```

2. If it is 'bdfh' the white colors will be in odd numbers
```python
return int(coordinates[1]) % 2 != 0
```