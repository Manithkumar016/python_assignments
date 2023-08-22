# 5) Write a Python class to find the three elements that sum to zero from a set of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]] 

list =[-25, -10, -7, -3, 2, 4, 8, 10]
class ZeroList:
    def __init__(self,list) :
        self.list=list
    def zerolist(self):
        list1=[]
        list2=[]
        list3=[]
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                for k in range(len(self.list)):
                    if self.list[i]+self.list[j]+self.list[k]==0 and self.list[i] not in list3 and self.list[j] not in list3 and self.list[k] not in list3:
                        list3.append(list[i])
                        list3.append(list[j])
                        list3.append(list[k])
                        list2.append(list[i])
                        list2.append(list[j])
                        list2.append(list[k])
                        list1.append(list2)
                        list2=[]

        print(list1)
ZL=ZeroList(list)
ZL.zerolist()
 


