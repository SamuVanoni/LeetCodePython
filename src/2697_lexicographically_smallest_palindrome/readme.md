## What Did I Learn?

### In this challenge I leraned more about logic:

1. We go through the entire word with two pointers and if the letters are different we switch to the smallest element.
```python
if s[i] != s[j]:
    if s[i] < s[j]:
        s[j] = s[i]
    elif s[i] > s[j]:
        s[i] = s[j]
```