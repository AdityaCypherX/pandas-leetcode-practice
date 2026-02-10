"""
Problem ID: 2886
Title: Change Data Type
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Type Conversion | Data Types
"""
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"]=students["grade"].astype(int)
    return students
