"""
Problem ID: 2885
Title: Rename Columns
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | DataFrame Structure | Renaming
"""
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:

    return students.rename(columns={"id":"student_id","first":"first_name","last":"last_name","age":"age_in_years"})
    
