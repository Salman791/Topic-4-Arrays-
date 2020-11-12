# - Create an array variable named `numList` with the following content:
#   `[3, 4, 5, 6, 7]`
# - Double all the values in the array

# numList = [3,4,5,6,7]
# i = 0
# #double_numList = numList
#
# for number in numList:
#     numList[i] = number * 2
#     #print(number)
#     i += 1
#     print(i)

list = [3,4,5,6,7]

for number in range(0,5):
    value = list[number]
    new_value = value * 2
    list[number] = new_value
    #list[number] = list[number]*2
print(list)
