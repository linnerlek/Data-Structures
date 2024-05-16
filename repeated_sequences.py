# Linn Erle Klofta
# CSC 2720 Homework #4
# Lab time: Friday 1-1:50pm
# Due time: 04/09/2024 @ 11:59pm

def findRepeatedSequences(s):
    # Create a dictionary to store the count of each 10-letter sequence
    sequences = {}
    result = []
    
    # Iterate through the string, considering each 10-letter sequence
    for i in range(len(s) - 9):
        sequence = s[i:i+10]
        
        # If the sequence is already in the dictionary, increment its count
        if sequence in sequences:
            sequences[sequence] += 1
        else:
            sequences[sequence] = 1
    
    # Iterate through the dictionary and add the repeated sequences to the result
    for sequence, count in sequences.items():
        if count > 1:
            result.append(sequence)
    
    return result

# Test cases
s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedSequences(s1))  # Output: ["AAAAACCCCC", "CCCCCAAAAA"]

s2 = "AAAAAAAAAAAAA"
print(findRepeatedSequences(s2))  # Output: ["AAAAAAAAAA"]