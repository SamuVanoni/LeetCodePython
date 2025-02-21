## What Did I Learn?

### In this challenge I learned:

1. Ensuring that Word S1 is smaller than s2
```python
if len(s1) > len(s2):
    continue
```

2. Taking the last/first elements of s2
```python
pre = s2[:len(s1)]
suf = s2[-len(s1):]
```

3. Comparing the values ​​found
```python
if pre == s1 and suf == s1:
    ans += 1
```