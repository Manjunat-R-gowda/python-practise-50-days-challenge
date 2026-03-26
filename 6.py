dic={"name":"manjunath","age":18,"city":"hassan"}
print(dic)
print(len(dic))



p=dic["name"]
print(p)

dic["email"]="manju@123"
print(dic)

dic["age"]=19
print(dic)

p="salary" in dic
print(p)

print(dic.keys())
print(dic.values())
print(dic.items())

d={"age":17}
a={"age":18}
d.update(a)
print(d)

num={1,2,5,6,7,8,9,45,6}
print(max(num))




