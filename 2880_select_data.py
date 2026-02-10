"""
Problem ID: 2880
Title: Select Data
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Data Selection | Filtering
"""
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"]==101,["name","age"]]
