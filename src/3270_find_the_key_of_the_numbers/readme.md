## What Did I Learn?

### In this challenge I learned:

1. Creating a function to add zeros until 4 characters
```python
def padding(num):
    st = str(num)
    while len(st) < 4:
        st = "0" + st
    return st
```

2. Adding the smallest numbers to the answer
```python
for i in range(4):
    ans += str(min(int(p[i]), int(q[i]), int(r[i])))
```