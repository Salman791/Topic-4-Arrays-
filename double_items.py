# - Create an array variable named `numList` with the following content:
#   `[3, 4, 5, 6, 7]`
# - Double all the values in the array

numList = [3,4,5,6,7]

double_numList = numList

for number in numList:
    double_numList = number ** 2
print(double_numList)
