import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


arr1 = np.array([1, 2, 3, 4])
print("Original array:", arr1)

a = [True, False, False, True]
b = arr1[a]

print("Filtered array:", b)

#-----------------------------
print('-------------------------------')

arr2 = np.array([3, 2, 0, 1])

print("Original array:", arr2)
print("Sorted array:", np.sort(arr2))

#-----------------------------
print('-------------------------------')

arr3 = np.array([1, 1, 2, 3, 4, 1])
print("Original array:", arr3)

c = np.where(arr3==1)

print("Index of element 1:", c)




a_dict = {'1st': 1, '2nd': 3, '3rd': 5, '4th':7, '5th': 9}
ser = pd.Series(a_dict)
ser

print('Range access:')
print(ser[0:3])

print('Access: Index number')
print(ser[1])

print('Access: Index label')
print(ser['2nd'])


data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)