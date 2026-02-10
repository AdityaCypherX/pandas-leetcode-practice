"""
Problem ID: 2881
Title: Create a New Column
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Column Operations | Feature Engineering
"""
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"]=employees["salary"]*2
    return employees
