
# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 

numbers= [90, 20,10,40,50,60,70]

class Target:
    def __init__(self,numbers) -> None:
        self.numbers=numbers
    def terget_reach(self):
        target=50
        n=0
        m=0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i]+self.numbers[j]==target:
                    n=i+1
                    m=j+1
                    break
        print(f"({m},{n})")

tar = Target(numbers)

tar.terget_reach()