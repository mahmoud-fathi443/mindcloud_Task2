import numpy as np

m, n = [int(i) for i in input("").split()]

matrix = []
decoded_string = ""
for i in range(m): # takes the input and stores them into an array
        user_input = input("")
        elements = user_input + " " * ((" " not in user_input) and (len(user_input) < n)) # checks if the string is n long if not adds a space at the end 
        elements = np.array(list(elements))
        matrix.append(elements)
matrix = np.array(matrix)


for i in range(n): # loops through the rows
        lst = matrix[0:, i] 
        for j in range(m):
                decoded_string += (lst[j] * (lst[j].isalnum())) + " " * ((not lst[j].isalnum()) and lst[j-1].isalnum()) # checks if the charracter is alphanumeric to add it and if it is not to add a space

print(decoded_string)
                