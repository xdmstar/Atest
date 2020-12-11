t=0
i=0
while True:
    z=input("请输入数字或e：")
    if z == "e":
        break
    i=i+1
    t+=float(z)
if i!=0:
    print(t,t/i)
if i==0:
    print(t,0)