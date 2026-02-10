"""
Problem ID: 2887
Title: Fill Missing Data
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Data Cleaning | Imputation
"""
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"]=products["quantity"].fillna(0)
    return products
