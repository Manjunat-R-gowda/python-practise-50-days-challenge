t=("apple","banana","grapes")
print(t)
print(type(t))

print(t[0])
print(t[-1])
print(len(t))

print(t.count(1))
print(t.index("grapes"))

l=[1,3,4,5,6,7,8]
print(tuple(l))

m=(1,4,5,3,6)
print(m)

a=(1,2,3)
b=(4,5,6)
print(a+b)
print(a*3)

print(max(b))
print(min(b))
print(list(b))

print(sorted(a))

s={"abhi","manju","rakshi"}
print(s)
print(type(s))

s.add("ravi")
print(s)

s.remove("ravi")
print(s)

p="manju" in s
print(p)

print(len(s))

m={ }
print(m)

l=[2,3,4,5,61,2,3,4]
print(l)
print(set(l))
s=l.remove(2)
print(s)

s={2,3,4}
n={4,5,6,1}
print(s|n)
print(s&n)
print(s-n)
print(s^n)

s.clear()
print(s)