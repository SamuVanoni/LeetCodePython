## What Did I Learn?

### In this challenge I learned:

1. Dictionary to store the number and the places it appears
```python
group_map = {}
    for i, size in enumerate(groupSizes):
        if size in group_map:
            group_map[size].append(i)
        else:
            group_map[size] = [i]
    #print(group_map) {1: [5], 3: [0, 1, 2, 3, 4, 6]}
```
2. Loop goes through the group list, grouping people into sublists of size size
```python
for size, group in group_map.items(): # 1 - [5] / 3 - [0, 1, 2, 3, 4, 6]
    for i in range(0, len(group), size):
        result.append(group[i:i+size])
```