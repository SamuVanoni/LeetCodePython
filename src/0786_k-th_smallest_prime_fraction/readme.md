## What Did I Learn?

### In this challenge:

1. We created two lists, one to store the division value and another to store the respective values ​​that we divided
```python
l.append(c) # [0.5, 0.3333333333333333, 0.2, 0.6666666666666666, 0.4, 0.6]
s.append([a,b]) # [[1, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 5]]
```

2. Then we link one list to another and sort by what we want to sort
```python
d=dict(zip(l,s)) # Link one list to another
# {0.5: [1, 2], 0.2: [1, 5], 0.4: [2, 5], 0.6: [3, 5], 0.3333333333333333: [1, 3], 0.6666666666666666: [2, 3]}
l.sort() # [0.2, 0.3333333333333333, 0.4, 0.5, 0.6, 0.6666666666666666]
```

3. We return the value according to the order in which we did the sort
```python
return d[l[k-1]]
```