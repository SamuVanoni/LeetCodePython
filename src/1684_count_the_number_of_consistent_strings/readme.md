## What Did I Learn?

### In this challenge I learned how to mix a condition with a loop:

1. Set for faster searches
```python
allowed_set = set(allowed)
```

2. If all letter elements are in authorized_set
```python
if all(letter in allowed_set for letter in word):
```
Letter being each letter present in word