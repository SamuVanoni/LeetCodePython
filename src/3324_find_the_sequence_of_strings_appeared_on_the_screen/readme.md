## What Did I Learn?

### In this challenge I learned:

1. This loop adds 'a' to the end of the string
```python
for c in target:
    s += 'a'
    result.append(s)
```

2. This loop adjusts the last char ('a') until it is the same as the target char
```python
while s[-1] != c:
    last_char = s[-1]
    last_char = chr(ord(last_char) + 1) if last_char != 'z' else 'a'
    s = s[:-1] + last_char
    result.append(s)
```