import random


def printBoard():
    for i in range(1,10):
        if(i%3==0):
            print(arr[i])
        else:
            print(arr[i],end="|")


arr=[0,1,2,3,4,5,6,7,8,9]
print("if you want play with computer enter pc else enter friend : ")
choise=input()
while(choise != "pc" and choise!= "friend"):
    print("wrong , please enter small character ")
    choise = input()
if (choise=="pc"):
    counter=0
    #printBoard()
    while(counter<=8):
        printBoard()
        print(" enter number from 1 to 9 : ")
        num=input()
        try:
            num=int(num)
        except:
            print("wrong , please enter  correct number")
            continue
        while (num<0 or num>9):
            print("wrong")
            printBoard()
            print(" enter number from 1 to 9 : ")
            num=input()
            try:
                num=int(num)
            except:
                print("wrong , please enter  correct number")
                continue
        test=0
        for i in range (1,10):
            if (num==arr[i]):
                arr[i]='X'
                test=1
        while(test==0):
            print("wrong")
            printBoard()
            print(" enter number from 1 to 9 : ")
            num=input()
            try:
                num=int(num)
            except:
                print("wrong , please enter  correct number")
                continue
            for i in range (1,10):
                if (arr[i]==num):
                   arr[i]='X'
                   test=1
        if((arr[1]==arr[2]==arr[3])or(arr[4]==arr[5]==arr[6])or(arr[7]==arr[8]==arr[9])or(arr[1]==arr[4]==arr[7])or(arr[2]==arr[5]==arr[8])or(arr[3]==arr[6]==arr[9])or(arr[1]==arr[5]==arr[9])or(arr[3]==arr[5]==arr[7])):
            printBoard()
            print("you win")
            break
        counter+=1
        if (counter>8):
            break
        j=1
        while(j<10):
            flag=0
            if(arr[j]==arr[j+1])and (arr[j+2]!='O' and arr[j+2]!='X') :
                arr[j+2]='O'
                flag=1
                break
            elif(arr[j+1]==arr[j+2])and (arr[j]!='O' and arr[j]!='X'):
                arr[j]='O'
                flag=1
                break
            elif(arr[j]==arr[j+2]) and (arr[j+1]!='O' and arr[j+1]!='X'):
                arr[j+1]='O'
                flag=1
                break
            j+=3
        for k in range (1,4):
            if(arr[k]==arr[k+3]) and (arr[k+6]!='O' and arr[k+6]!='X')and (flag==0):
                arr[k+6]='O'
                flag=1
                break
            elif(arr[k+3]==arr[k+6]) and (arr[k]!='O' and arr[k]!='X')and (flag==0):
                arr[k]='O'
                flag=1
                break
            elif(arr[k]==arr[k+6]) and (arr[k+3]!='O' and arr[k+3]!='X')and (flag==0):
                arr[k+3]='O'
                flag=1
                break
        if(arr[1]==arr[5]) and (arr[9]!='O' and arr[9]!='X')and (flag==0):
            arr[9]='O'
            flag=1
        elif(arr[5]==arr[9]) and (arr[1]!='O' and arr[1]!='X')and (flag==0):
            arr[1]='O'
            flag=1
        elif(arr[1]==arr[9]) and (arr[5]!='O' and arr[5]!='X')and (flag==0):
            arr[5]='O'
            flag=1
        if(arr[3]==arr[5]) and (arr[7]!='O' and arr[7]!='X')and (flag==0):
            arr[7]='O'
            flag=1
        elif(arr[5]==arr[7]) and (arr[3]!='O' and arr[3]!='X')and (flag==0):
            arr[3]='O'
            flag=1
        elif(arr[3]==arr[7]) and (arr[5]!='O' and arr[5]!='X')and (flag==0):
            arr[5]='O'
            flag=1
        if(flag==0):
            test=0
            while(test==0):
                num= random.randint(1,10)
                for i in range (1,10):
                    if (arr[i]==num):
                        arr[i]='O'
                        test=1
        if((arr[1]==arr[2]==arr[3])or(arr[4]==arr[5]==arr[6])or(arr[7]==arr[8]==arr[9])or(arr[1]==arr[4]==arr[7])or(arr[2]==arr[5]==arr[8])or(arr[3]==arr[6]==arr[9])or(arr[1]==arr[5]==arr[9])or(arr[3]==arr[5]==arr[7])):
            printBoard()
            print("computer win")
            break
        counter+=1
    if(counter>8):
        print("no winner")
elif(choise=="friend"):
    print("player 1 choise x or o")
    choise=input()
    flag=1
    while(flag==1):
        if(choise=='x' or choise=='X'):
            player1='X'
            player2='O'
            flag=0
        elif(choise=='o' or choise=='O'):
            player1='O'
            player2='X'
            flag=0
        else:
            print("wrong choise")
            print("please choise x or o")
            choise=input()
    printBoard()
    counter=0
    while(counter<=8):
        print("player 1 , enter number from 1 to 9 : ")
        num=input()
        try:
            num=int(num)
        except:
            print("wrong , please enter  correct number")
            continue
        while (num<0 or num>9):
            print("wrong")
            printBoard()
            print("player 1 , enter number from 1 to 9 : ")
            num=input()
            try:
                num=int(num)
            except:
                print("wrong , please enter  correct number")
                continue
        test=0
        for i in range (1,10):
            if (arr[i]==num):
               arr[i]=player1
               test=1
        while(test==0):
            print("wrong")
            printBoard()
            print("player 1 , enter number from 1 to 9 : ")
            num=input()
            try:
                num=int(num)
            except:
                print("wrong , please enter  correct number")
                continue
            for i in range (1,10):
                if (arr[i]==num):
                   arr[i]=player1
                   test=1
        printBoard()
        if((arr[1]==arr[2]==arr[3])or(arr[4]==arr[5]==arr[6])or(arr[7]==arr[8]==arr[9])or(arr[1]==arr[4]==arr[7])or(arr[2]==arr[5]==arr[8])or(arr[3]==arr[6]==arr[9])or(arr[1]==arr[5]==arr[9])or(arr[3]==arr[5]==arr[7])):
            print("player 1 win")
            break
        counter+=1
        if (counter>8):
            break
        print("player 2 , enter number from 1 to 9 : ")
        num=input()
        try:
            num=int(num)
        except:
            print("wrong , please enter  correct number")
            continue
        counter+=1
        while (num<0 or num>9):
            print("wrong")
            printBoard()
            print("player 2 , enter number from 1 to 9 : ")
            num=input()
            try:
                num=int(num)
            except:
                print("wrong , please enter  correct number")
                continue
        test=0
        for i in range (1,10):
            if (num==arr[i]):
                arr[i]=player2
                test=1
        while(test==0):
            print("wrong")
            printBoard()
            print("player 2 , enter number from 1 to 9 : ")
            num=input()
            try:
                num=int(num)
            except:
                print("wrong , please enter  correct number")
                continue
            for i in range (1,10):
                if (arr[i]==num):
                   arr[i]=player2
                   test=1
        printBoard()
        if((arr[1]==arr[2]==arr[3])or(arr[4]==arr[5]==arr[6])or(arr[7]==arr[8]==arr[9])or(arr[1]==arr[4]==arr[7])or(arr[2]==arr[5]==arr[8])or(arr[3]==arr[6]==arr[9])or(arr[1]==arr[5]==arr[9])or(arr[3]==arr[5]==arr[7])):
            print("player 2 win")
            break
    if(counter>8):
        print("no winner")
    
