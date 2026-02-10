"""
Problem ID: 2889
Title: Reshape Data: Pivot
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Reshaping | Pivot
"""
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
   return weather.pivot(index="month", columns="city", values="temperature")
