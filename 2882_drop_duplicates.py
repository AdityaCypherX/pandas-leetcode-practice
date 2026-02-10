"""
Problem ID: 2882
Title: Drop Duplicate Rows
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Data Cleaning | Duplicates
"""
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset="email",keep="first")
