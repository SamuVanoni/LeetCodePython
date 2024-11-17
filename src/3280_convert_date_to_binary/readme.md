## What Did I Learn?

### In this challenge I learned:

1. use map to separate the date string into integers when encountering a '-'
```python
y, m, d = map(int, date.split('-'))
```

2. Transform into binary by removing the '0b' that Python puts at the beginning
```python
ybin = bin(y)[2:]
```