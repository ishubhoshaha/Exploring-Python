import sys
print("Python Version:")
print(sys.version)

# Create List 
num = [i for i in range(15)]
print(num)

# Create List which consist only even numbers
even = [i for i in num if i % 2 == 0]
print(even)

# Create List of Tuples which consist of permutations between "abcd" and num list
mixed = [(letter, i) for letter in "abcd" for i in num if i % 2 == 0]
print(mixed)

#Extracting String 
letters = [letter for letter in "abcdefgh"]
print(letters)

#Creating Dictionary
d = {letter: value for letter, value in zip(letters, even)}
print(d)
