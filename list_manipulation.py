# Linn Erle Klofta
# CSC 2720 Homework #2
# Lab time: Friday 1-1:50pm
# Due time: 02/20/2024 @ 11:59pm


def has_duplicates_word_finder(n, words):
    # Convert the list of words to a set to remove duplicates
    unique_words = set(words)

    # If the length of the set is less than the length of the original list,
    # it means there were duplicates
    if len(unique_words) < len(words):
        return True
    else:
        return False


def sort_flowers(n, flowers):
    # Perform bubble sort
    for i in range(n - 1):
        for j in range(n - i - 1):
            if flowers[j] > flowers[j + 1]:
                flowers[j], flowers[j + 1] = flowers[j + 1], flowers[j]

    return flowers


def reverse_list(lst):
    # Initialize two pointers, one at the beginning and one at the end of the list
    start = 0
    end = len(lst) - 1

    # Swap elements at the start and end pointers until they meet in the middle
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst

# Test cases


print(has_duplicates_word_finder(
    5, ['spring', 'summer', 'fall', 'summer', 'winter']))  # True
print(has_duplicates_word_finder(
    4, ['spring', 'summer', 'fall', 'winter']))  # False

print(sort_flowers(3, ['Rose', 'Lily', 'Tulip']))  # ['Lily', 'Rose', 'Tulip']
# ['Daisy', 'Orchid', 'Rose', 'Sunflower', 'Tulip']
print(sort_flowers(5, ['Sunflower', 'Daisy', 'Orchid', 'Tulip', 'Rose']))

print(reverse_list([3, 4, 7, 6, 1]))  # [1, 6, 7, 4, 3]
print(reverse_list([1]))  # [1]
print(reverse_list([]))  # []
