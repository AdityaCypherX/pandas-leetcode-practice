"""
Problem ID: 2891
Title: Method Chaining
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | DataFrame Filtering | Sorting | Method Chaining
"""
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[["name"]]
