
# pattern printing

# using fn

def patt(rows):

    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=" ")
        print()
    for i in range(1,rows+1):
        for j in range(0,i):
            print("*",end=" ")
        print()

rows = 5
patt(rows)
