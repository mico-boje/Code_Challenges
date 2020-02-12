# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
def code_challenge(array, k):
    llen = len(array)
    i = -1
    while i < llen:
        o = 0
        i += 1
        if i >= llen:
            break
        while o < llen:
            if i == o:
                o += 1
                continue
            else:
                tu = array[i]+array[o]
                o += 1
                if tu == k:
                    return True

#Given an array of integers, find the first missing positive integer in linear time and constant space. 
#In other words, find the lowest positive integer that does not exist in the array. 
#The array can contain duplicates and negative numbers as well.
def code_challenge2(array):
    for i, e in enumerate(sorted(array)):
        
    


list1 = [10, 15, 3, 3]
list2 = [10, 8, 50, -2,0, 1,2,3,4,5,5]
k = 17
#print(code_challenge(list1, k))
print(code_challenge2(list2))