#1
n=int(input("enter number "))
def numbers(x):
    if x%2==0:
        return 0
    if x%2!=0:
        return 1

print(numbers(n))


#2

def average(n):
    count = 0
    total = 0
    for i in range(n):
        n=int(input("enter number"))
        count+=1
        total+=n
    return (total/count)
print(average(3))


#3

def num():
    x = input("enter number")
    while x !="-999":
        print(len(x))
        x = input("enter number")
num()


#4

count20=0
count10=0
count5=0
count1=0

def change(money):
    x=money//20
    coins=money-(x*20)
    y=coins//10
    coinsof5=money-(x*20+y*10)
    b=coinsof5//5
    coins0f1=money-(x*20+y*10+b*5)
    n=coins0f1//1
    return ("שטרות של 20=",x,"מטבעות של 10=",y,"מטבעות של 5=",b,"מטבעות של 1=")

print(change(76))

#5

def numbers(x,y):
    return x**y

print(numbers(2,2))


#6

def discount(x):
    return x-(x * 0.2)

def price(x):
    if x>1000:
        return discount(x)

    else:
        return x-(x*0.1)

print(price(900))



#9

def numbers(x,y):
    x=int(input("enter number"))
    y=int(input("enter number"))


#11
def special_care():
    cus_num=int(input("customer number"))
    a=int(input("value for year"))
    b=int(input("did you pay on time?:1-yes,0-no"))
    c=int(input("how many years did you buy here?"))

    if a>8000 and b==1 or c>5 :
        print(cus_num,"you deserved special care")
    if b==1 and c>5 or b==1:
        print(cus_num,"you deserved special care")

special_care()

