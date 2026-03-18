l=["fruit","apple"]
l.append("grapes")
print(l)
b=l.insert(1,"arun")
print(b)
print(l.index("fruit"))
l.remove("fruit")
print(l)

l.pop(1)
print(l)

l.clear()
print(l)

l.copy()
print(l)



print(l)
print(type(l))

print(len(l))

num=[2,4,5,6,7,4]
print(num)
print(num[0])
print(num[-1])

num[0]=100
print(num)

num[5]=100
print(num)

print(num[1:3])
print(num[2: :])
print(num[:-1])

print(num[1:2:2])
print(len(num))

print(sorted(num))
print(sum(num))

print(num.count(2))
print(num.reverse())

num=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(num)
print(num[1])
