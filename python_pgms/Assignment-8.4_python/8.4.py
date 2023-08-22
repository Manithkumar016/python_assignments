# This is problem to convert all the negative coordinates to a positive coordinates;
# The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
# We can add or delete any number from the coordinates ; however graph should not be changed;

# Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
# Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]

list=[(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]

def pos_list(list):
    min=0
    for i in range(len(list)):
        for j in range(2):
            if list[i][j]<min:
                min=list[i][j]
                
    min = -min
    print(min)
    list2=[]
    for i in range(len(list)):
        list2.append((list[i][0]+min,list[i][1]+min))
    return list2

print(pos_list(list))

