size = input("how big is the pyramid ? ")
size = int(size)
for x in range(1, (size)):
    #if x < size:
    print(((size) -(x))*" ", x*'#', "  ", x*'#')
    ##else:
        #print(x*'#', "  ", x*'#')
print("    ","#" *-4)