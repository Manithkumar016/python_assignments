import random



def word_guess():
    f = open("./Assignment-8.2_python/myfile.txt","r")
    n=f.read().split("\n")

    x=random.choice(n)
    # print(x)
    count=0
    for i in x:
        list=[]
        m=input("guess the letter: ")
    
        if i.upper()==m.upper():
            print("correct")
            list=[]
        else:
            while(len(list)!=6):
                if m not in list:
                    list.append(m)
                print(f"guesses left {6-len(list)}")
                m=input("try again: ")
                if i.upper()==m.upper():
                    print("correct")
                    list=[]
                    break
                else:
                    if m not in list:
                        list.append(m)
            if len(list)==6:
                # print("you loose")
                print(x)
                return False
                break
    return True
while True:
    
    choice=int(input("1.start the game\n2.Quit: \nenter your choice: "))
    if choice==1:
        b=word_guess()
        if b:
            print("you won 🥳🥳")
        else:
            print("you lost 😵😵")
    elif choice==2:
        exit(0)
    else:
        print("invalid choice")

               