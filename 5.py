dic={"name":"manjunath","age":18,"village":"hassan"}
print(dic)
print(type(dic))

print(dic.get("name"))
dic["age"]=19
print(dic)

m=dic.pop("name")
print(m)

"age"in dic
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())
print(len(dic))

new={"age":19}
dic.update(new)

s1={"a":1,"b":2}
s2={"c":4,"d":5}
s1.update(s2)
print(s1)

res=s1 |s2
print(res)

print(max(s1))
print(min(s2))



