## What Did I Learn?

### In this challenge I lerned:

1. How to store the last occurrence
```python
find = {'G': -1, 'P': -1, 'M': -1}
for i in range(len(garbage) - 1, -1, -1):
    if 'G' in garbage[i] and find['G'] == -1:
        find['G'] = i
    if 'P' in garbage[i] and find['P'] == -1:
        find['P'] = i
    if 'M' in garbage[i] and find['M'] == -1:
        find['M'] = i
```

2.  Sum the travel time to the found index
```python
for key, index in find.items():
    if index != -1:
        ans += sum(travel[:index])
```