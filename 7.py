i=0
while i<10:
    i+=1
    print(i)

i=10
while i>0:
    i-=1
    print(i)

i=5
while i%2==0:
    print("even number")
    break
else:
    print("this is not even number")

while True:
    i=int(input("enter your number:-"))
    if i%2!=0:
        print("odd number")
    else:
        print("this is even number")
    break

n=1
sum=0
while n<10:
    n+=1
    sum+=n
print(sum)

i=1
j=5
while i<10:
    i+=1
    print(f"{j*i}")

i=10
count=0
while i>0:
    i=i//10
    count+=1
    
print(count)    


num=int(input("enter a number:-"))
i=0
while num<0:
    num=num%10
    num=num//10
    reverse=reverse+num/num
print(reverse)

    