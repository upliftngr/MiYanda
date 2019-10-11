# numbers = range(1,10)
# even = []
# for i in numbers:
    
#     if i%2 ==0:
#         even.append(i)
# print (even)


even = [x for x in range(1,10) if x%2 == 0]
print(even) 