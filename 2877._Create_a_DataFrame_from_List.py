"""
Problem ID: 2877
Title: Create a DataFrame from List
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | DataFrame Creation | Basics
"""
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df=pd.DataFrame(student_data,columns=["student_id","age"])
    return df
    
