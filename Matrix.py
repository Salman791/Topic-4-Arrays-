# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

list1 = [0,0,0,0]
line_number = 0

for line_number in range(0,4):
    list1[line_number] += 1 # add increment to each value
    print(list1[0], list1[1], list1[2], list1[3]) # print items individually rather than a list

    list1[line_number] -= 1 # change to 0 again

