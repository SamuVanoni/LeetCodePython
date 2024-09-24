## What Did I Learn?

### In this challenge I learned how to count the number of times a word appears and how to order a list by the largest number:

1. Counting the number of times a word appears
```python
freq = Counter(word).values()
```

2. Sorting according to the largest values
```python
sorted_freq = sorted(freq, reverse=True)
```

3. Loop that does the sum for the result variable
```python
for n in sorted_freq:
    result += n * (i // 8 + 1)
    i += 1
```