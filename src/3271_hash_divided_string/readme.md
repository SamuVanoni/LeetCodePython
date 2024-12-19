## What Did I Learn?

### In this challenge I learned:

1. We had to do a while loop with limit range breaking check
```python
while count < k and (i + count) < len(s):
```

2. Making the sum of the letters
```python
countSum += ord(s[i + count].lower()) - ord('a')
```

3. Converting the resulting sum into the respective letter
```python
ans += chr(ord('a') + (countSum % 26))
```