## What Did I Learn?

### In this challenge I learned about mapping:

1. Initializing mapping
```python
mapping = {' ': ' '}
```

2. Create mapping
```python
i = 0
letters = 'abcdefghijklmnopqrstuvwxyz'

for char in key:
    if char not in mapping:
        mapping[char] = letters[i]
        i += 1
```

3. Using mapping
```python
res = ''
for char in message:
    res += mapping[char]
```