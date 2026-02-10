"""
Problem ID: 2884
Title: Modify Columns
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Column Modification | Type Casting
"""
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"]=employees["salary"]*2
    return employees
