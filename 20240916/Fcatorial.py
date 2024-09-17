def find_fact(N):
    fact=1
    for I in range(N,1,-1):
        fact=fact* I 
    return fact

f1=find_fact(5)
f2=find_fact(4)
f3=find_fact(3)
print(f1)
print(f2)
print(f3)
