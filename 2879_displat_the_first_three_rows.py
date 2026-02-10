"""
Problem ID: 2879
Title: Display the First Three Rows
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Data Inspection | Head
"""
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
