## What Did I Learn?

### In this challenge I learned:

1. Creating a start and end variable for loops
```python
start = 1
end = 7
```

2. Creating a loop to have 7 full numbers. Increase the start and end as needed.
```python
while (n - 7) > 0:
    for i in range(start, end+1):
        ans += i
    start += 1
    end += 1
    n -= 7
```

3. Loop case on number less than 7
```python
while n != 0:
    ans += start
    start += 1
    n -= 1
```