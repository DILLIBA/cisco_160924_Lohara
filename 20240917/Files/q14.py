import json


num_list=[int(num) for num  in input('enter the unique integer numbers with space: ').split()]
num_set=set(num_list)
num_fset=frozenset(num_set)
num_dict={num:num*num*num for num in num_fset}
print(f'Dictionary: {num_dict}')
with open('q14.json','w') as q14_db:
    json.dump(num_dict,q14_db)
with open('q14.json','r')as q14_db:
    read_num=json.load(q14_db)
    print(f'read Dictionary: {read_num}')