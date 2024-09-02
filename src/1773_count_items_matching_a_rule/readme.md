## What Did I Learn?

### In this challenge I learned a new solution to this problem:

1. Create a dictionary
```python
d = {'type': 0, 'color': 1, 'name': 2}
```

2. If 'item[d[ruleKey]] == ruleValue' it adds 1 to the count
```python
return sum(1 for item in items if item[d[ruleKey]] == ruleValue)
```