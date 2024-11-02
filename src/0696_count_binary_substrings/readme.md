## What Did I Learn?

### In this challenge I learned more about logic:

1. First we count how many consecutive 0s and 1s we have and store them in groups
```python
groups = []
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        groups.append(count)
        count = 1
groups.append(count)  # Add the last group
# print(groups) => [2, 2, 2, 2] two 0, two 1, two 0, two 1
```

2. Then we take 2 in 2 groups and add the answer to the smallest of the stored numbers
```python
ans = 0
for i in range(1, len(groups)):
    ans += min(groups[i - 1], groups[i])  # Form pairs with groups
```