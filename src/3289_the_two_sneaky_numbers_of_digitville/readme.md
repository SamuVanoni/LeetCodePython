## What Did I Learn?

### In this challenge I learned :

1. Create a dictionary and add values to it
```python
d = {}
for n in nums:
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1
```

2. Find the maxValue and return all values == maxValue
```python
maxValue = max(d.values())
return [r for r, value in d.items() if value == maxValue] 
```