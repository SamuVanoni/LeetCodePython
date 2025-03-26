## What Did I Learn?

### In this challenge I learned more about logic:

1. We count the open relatives, regardless of the situation.
```python
if c == "(":
    open_brackets += 1
```

2. If we close a parenthesis, we find if there is an open; If so, we reduce the count. If not, we recorded an incorrect closed parenthesis.
```python
else:
    if open_brackets > 0:
        open_brackets -= 1
    else:
        min_adds_required += 1
```