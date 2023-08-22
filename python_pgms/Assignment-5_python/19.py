# 19. From a list containing ints, strings and floats, make three lists to store them separately

list=[1,"world",1.23]
list_i=[]
list_s=[]
list_f=[]

for i in list:
    if type(i)==int:
        list_i.append(i)
    elif type(i)==str:
        list_s.append(i)
    else:
        list_f.append(i)

print(list_i,"\n")
print(list_s,"\n")
print(list_f,"\n")