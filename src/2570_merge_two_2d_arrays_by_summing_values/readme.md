## What Did I Learn?

### In this challenge I learned more about dictionary:

1. We start by adding the elements to the dictionary according to the key. If the dictionary already has the key, we add the value to it.
```python
for num1 in nums1:
    d[num1[0]] = num1[1]
for num2 in nums2:
    if num2[0] not in d:
        d[num2[0]] = num2[1]
    else:
        d[num2[0]] += num2[1]
```

2. Then we transform the dictionary into a list and sort by key to return the answer.
```python
result = [[key, value] for key, value in d.items()]
result.sort(key=lambda x: x[0])
```