#recursion
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5) #5,4,3,2,1

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1)*n
# print(fact(4))

#Write a recursive function to calculate the sum of first n natural numbers.

# def sum(n):
#     if(n == 0):
#         return 0
#     return sum(n-1) + n
# sum1 = sum(5)
# print(sum1)


#Write a recursive function to print all elements in a list.
#Hint : use list & index as parameters.

# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# number = [1,2,3,4,5,6,7,8,9]

# print_list(number)


