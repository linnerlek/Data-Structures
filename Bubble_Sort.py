# Linn Erle Klofta
# CSC 2720 Lab #3
# Lab time: Friday 1-1:50pm
# Due time: 01/28/2024 @ 11:59pm

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

input_list = [50, 11, 33, 21, 40, 50, 40, 40, 21]
output_list = bubble_sort(input_list)
print(output_list)
