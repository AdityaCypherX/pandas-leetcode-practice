"""
Problem ID: 2888
Title: Reshape Data: Concatenate
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Reshaping | Concatenation
"""
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2],ignore_index=True)
