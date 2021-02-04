# patern printing 2
#
# rows=7
#
# for i in range(1, rows + 1):
#     for j in range(0, i):
#         print(i, end=" ")
#     print()

# for i in range(1, rows + 1):
#     for j in range(0, i):
#         i=rows=i
#         print(i, end=" ")
#     print()
#
#     for i in range(i,j):
#         rows = rows + 1
#         print()
# k = 1
#
# for i in range(0, 7):
#     for j in range(0, i + 1):
#
#         print(k, end=" ")
#         k = k + 1
#     print("")


num=7
for i in range(1, num):
    # num=
    for j in range(0, i+1):
        for i in range(j, num + i):

            print(i, end=" ")
            print()

