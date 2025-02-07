import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # .loc [] -> Access Dataframe lines and columns
    # Select ["name", "age"] if ["student_id"] == 101
    return students.loc[students["student_id"] == 101, ["name", "age"]]