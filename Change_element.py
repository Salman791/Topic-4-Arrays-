# - Create an array variable named `numbers`
#   with the following content: `[1, 2, 3, 8, 5, 6]`
# - Change the 8 to 4
# - Print the fourth element

numbers = [1, 2, 3, 8, 5, 6]
print(numbers)

for n, i in enumerate(numbers):
    if i == 8:
        numbers[n] = 4

print(numbers)