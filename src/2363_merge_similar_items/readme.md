## What Did I Learn?

### In this challenge I learned:

1. Remembering how to add and change elements in a dict
```python
freq = {}
for i in items1:
    if i[0] not in freq:
        freq[i[0]] = i[1]
    else:
        freq[i[0]] += i[1]
```

2. Return the items ordered by the first element (key)
```python
return sorted([[k, v] for k, v in freq.items()])
```