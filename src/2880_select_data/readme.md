## What Did I Learn?

### In this challenge I learned:

1. Use the .loc[] for access Dataframe lines and columns
```python
students.loc[]
```

2. Filtering ["name", "age"] if ["student_id"] == 101
```python
students.loc[students["student_id"] == 101, ["name", "age"]]
```