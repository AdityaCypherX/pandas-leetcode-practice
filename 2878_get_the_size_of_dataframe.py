"""
Problem ID: 2878
Title: Get the Size of a DataFrame
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | DataFrame Properties | Basics
"""
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return[players.shape[0],players.shape[1]]
    
