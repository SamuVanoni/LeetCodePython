## What Did I Learn?

### In this challenge I learned more about logic:

1. We start by storing all the first cities in each list
```python
cities = set()
for path in paths:
    cities.add(path[0])
```

2. Then we take the second city from each list and if it is not in the first list we return it
```python
for path in paths:
    dest = path[1]
    if dest not in cities:
        return dest
```