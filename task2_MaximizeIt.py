import itertools

k, m= list(map(int, input().split())) #takes the k, m input and castes them into an int

s = 0
k_lists = []

def f(x):
    return x**2

for i in range(k): # Stores the input into a 2D array
    n_list = list(map(int, input().split()))
    k_lists.append(n_list[1:])


combinations = itertools.product(*k_lists) # gets the combinations of the input lists

s_max = 0
for comb in combinations:
    square_sum = sum(f(x) for x in comb) # applies f(x) to each element of the list and gets the sum
    s = square_sum % m
    if s > s_max: # checks S_max if it is bigger than the previous one 
        s_max = s


print(s_max)


    
        
    
    

