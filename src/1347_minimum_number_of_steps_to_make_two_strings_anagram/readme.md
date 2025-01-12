## What Did I Learn?

### In this challenge I learned:

1. We create a list with 26 positions with values ​​= 0. We add/subtract values ​​according to the letter present in s or t
```python
count = [0] * 26
for i in range(len(s)):
    count[ord(s[i]) - ord('a')] += 1
    count[ord(t[i]) - ord('a')] -= 1
```

2. We count all elements that are above 0
```python
sum = 0
for n in count:
    if n > 0:
        sum += n
```