def cal(frist:int,second:int)->int:
    sum=frist+second
    diff=frist-second
    produ=frist*second
    quotient=frist//second
    return sum,diff,produ,quotient

s,d,p,q=cal(20,6)
print(s,d,p,q)

t1=cal(10,6)
print(t1)
print(type(t1))