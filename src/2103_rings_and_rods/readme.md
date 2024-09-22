## What Did I Learn?

### In this challenge I learned a new way of looping, how to store without repetitions and use sum() to return the answer:

1. A loop that goes from 2 to 2 and stores the color and ring variables
```python
for i in range(0, len(rings), 2):
    color = rings[i]
    ring = rings[i + 1]
```

2. Add the ring to the dictionary if it doesn't already have it, in a way that doesn't accept repetition (set)
```python
if ring not in ans:
    ans[ring] = set()
```

3. Add color to the ring
```python
ans[ring].add(color)
```

4. Adds 1 for each color in the rings and returns if = 3
```python
return sum(1 for colors in ans.values() if len(colors) == 3)
```