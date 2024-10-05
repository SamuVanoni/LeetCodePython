## What Did I Learn?

### In this challenge I lerned new functions:

1. We store in an array how many times each letter is repeated
```python
Counter(s).values()
```

2. We take the repeated values
```python
set(Counter(s).values())
```

3. If after removing the duplicates there is only 1 element left, we return true
```python
len(set(Counter(s).values())) == 1
```