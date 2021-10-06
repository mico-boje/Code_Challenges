# 7 kyu Highest and Lowest
from heapq import nlargest, nsmallest

def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return f"{nlargest(1, numbers)[0]} {nsmallest(1, numbers)[0]}"