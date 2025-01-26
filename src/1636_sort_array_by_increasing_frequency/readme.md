## What Did I Learn?

### In this challenge I learned:

1. Creating a dictionary where the keys are the elements of the nums list and the values ​​are the frequencies of occurrence of each element.
```python
freq = Counter(nums)
```

2. freq[x] -> Sorts the elements by frequency (in ascending order). -x -> For elements at the same frequency, it orders in a decreasing order of value.
```python
return sorted(nums, key=lambda x: (freq[x], -x))
```