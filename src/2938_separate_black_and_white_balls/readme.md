## What Did I Learn?

### In this challenge I learned a new form to solution a problem:

1. We don't actually exchange the elements, we just do the counting we need for the answer
```python
swaps += ri - li
```

2. We decrease ri and increase li depending on whether the element is 0 or 1
```python
while li < ri:
    if s[li] == '1':
        if s[ri] == '0':
            li += 1
        ri -= 1
    else:
        if s[ri] == '1':
            ri -= 1
        li += 1
```