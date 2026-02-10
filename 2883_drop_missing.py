"""
Problem ID: 2883
Title: Drop Missing Values
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Data Cleaning | Missing Data
"""
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
