
# 19. Write a Python program to find smallest and largest word in a given string.

s="zq abc defg h"
x={}
t=s.split(" ")
max=0
m_word=""
min=len(t[0])
min_word=""
for i in t:
    if len(i)>max:
        max=len(i)
        m_word=i
    if len(i)<min:
        min=len(i)
        min_word=i
print("max word: ",m_word," min word: ", min_word)