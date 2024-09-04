## What Did I Learn?

### In this challenge I learned more about logic:

1. Here we store the largest value in maxVol by calculating the distance between right and left * the smallest value of the two bars
```python
maxVol = max(maxVol, (right - left) * min(height[left], height[right]))
```

2. Let's change the index depending on which is smaller
```python
if height[left] < height[right]:
        left += 1
    else:
        right -= 1
```