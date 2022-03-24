#1

def numbers():
    count=0
    total=0
    x = input("enter number")
    while x!='q':
        count += 1
        total += int(x)
        x=input("enter number")

    print(total/count)

numbers()
#

# #2

def palindrom(st):
    start=0
    end=len(st)-1
    for i in range(len(st)//2):
        if st[start]!=st[end]:
            print("not palindrom")
            return
        else:
            start+=1
            end-=1

    print("palindrom")

palindrom("anna")


#3

ls=[1,2,3,4,5,8]

def list(ls):
    for i in ls:
        if not i>0 and i is type(int):
            return "false"
    return "true"

print(list(ls))


# #4

def minutes(minutes):
    return minutes/60

print(minutes(90))

#5

def buli(x,y):

    if x==y:
        print("")
    else:
        print("false")

buli(3>8,2<1)


#6
ls = [1, 1, 7, 5, 5, 6, 8]
def count_numbers(ls):
    newls=[0,0,0,0,0,0,0,0,0,0]
    for i in ls:
        newls[i]+=1
    return newls

print(count_numbers(ls))