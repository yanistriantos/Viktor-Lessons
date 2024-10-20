
# for i in range(x + 1):
# for j in range(y + 1):
# for k in range(z + 1):
# if (i + j + k != n):
#     print(i, j, k)

# input
# x -> first number in the sublist 
# y -> secibd number in the sublist
# z -> third number in the sublist
# n -> x + y + z != n

# Step #1
# Create a matrix with all the sublists containing the permutations of x, y, z
# x = 2, 0 -> 1 -> 2
# y = 1, 0 -> 1
# z = 2, 0 -> 1 -> 2

# x, y, z = 1
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# ...

# x = 1, y = 2, z = 2
# 0 0 0
# 0 0 1
# 0 0 2
# 0 1 0
# 0 1 1
# 0 1 2
# 0 2 0
# 0 2 1 
# 0 2 2
# 1 0 0

x = 1
y = 2
z = 2
n = 3

l = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            # l.append([i, j, j])
            if i+j+k != n:
                l.append([i, j, k])
                
print(l)

# Output
# Matrix in which all the sublists' sum != n 

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
# x = 1
# y = 1
# z = 2 
# n = 3

# new_list = [(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# print(new_list)
               