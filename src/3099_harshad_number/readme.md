## What Did I Learn?

### In this challenge, I learned:

1. How to add the digits of an int easily
```python
soma = sum(int(d) for d in str(x))
```
Turn the int into a string, loop through each 'letter' turning it back into an int and performing the sum

2. How to create an if and else in one line (I did it alone!!)
```python
soma if x % soma == 0 else -1
```
Result you want if right + if + rule + else + result if wrong