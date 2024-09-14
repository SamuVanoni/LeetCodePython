## What Did I Learn?

### In this challenge:

1. Taking the respective value of each letter (a = 0, b = 1...) and searching for its value in the morse list
```python
morse[ord(letter) - ord("a")]
```

2. After storing all morse words in the ans list we use set() and len()
```python
len(set(ans))
```
`set()` eliminates repeated elements within a list. `len()` counts array elements.