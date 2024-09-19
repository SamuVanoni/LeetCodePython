## What Did I Learn?

### In this challenge I learned more about ASCII table:

1. Checking if it's a number
```python
if letter in numbers:
```

2. If it is a number we add it to the previous letter of the string (getting its value from the ASCII table)
```python
count = ord(s[i-1]) + int(letter)
```

3. Transforming the number we find into its respective value in the ASCII table
```python
ans += chr(count)
```