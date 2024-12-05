'''
Daniel, 8 Computer Science 
Assignment: Triangle.py 
Your assignment is to create a python program that prints a triangle that is 8 lines in height and 8 characters in width
'''

# Number of lines and width of the triangle
height = 8
width = 8

# Loop through each line
for i in range(1, height + 1):
    # Print the required number of characters for each line
    print('*' * i)
