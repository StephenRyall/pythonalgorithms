import math
import numpy as np

def equalizeArray(arr):
    return len(arr) - max(arr.count(i) for i in arr)
        
print(equalizeArray([1, 2, 3, 1, 2, 3, 3, 3]))