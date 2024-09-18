


# def cal_diff(frist:int=10,second:int=20):
#     return(frist-second)

# print(cal_diff(20,10))
# print(cal_diff(second=20,frist=10))
# print(cal_diff( ))
# print(cal_diff(second=10))

# def change_name(names,index,name):
#     names[index]=name

# names=['rahul','modi']
# print(names)
# change_name(names,0,'modiji')
# print(names)

# print([10,20,30])

""" def find_sum(frist,second, **others):
    s = frist+second
    if(len(others)>0):
      for key in others:
          s += others[key]

    return s
print(find_sum(frist=10,second=20)) 
print(find_sum(frist=10,second=20,third=30)) 
print(find_sum(frist=10,second=20,third=40,frouth=30))  """    

""" def fact(N):
     if N <=1:
      return 1
     return N* fact(N-1)
print(f'factorial of n is: {fact(5)}')
print(f'factorial of n is: {fact(4)}') """

import math


def is_prime(N): 
    N_sqrt= int(math.sqrt(N))
    for I in range(2 ,N_sqrt):
        if N % I == 0:
            return False
        

    return True
print(is_prime(5))
print(is_prime(51))
print(is_prime(60))
print(is_prime(61))
