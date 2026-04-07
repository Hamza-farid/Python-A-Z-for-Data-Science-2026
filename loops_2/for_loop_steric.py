# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end="")
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print()


# for i in range(1,6):
#     for j in range(6-i):
#         print("*", end="")
#     print()


rows = 5

for i in range(rows):
   spaces = " "*(rows-i-1)
   stars = "*"*(2*i+1)
   print(spaces + stars)

for i in range(rows):
   spaces = " "*i
   stars = "*"*(2*(rows-i)-1)
   print(spaces + stars)

   