int_list=[int(num) for num in input('enter the integer vaulues(space):').split()]
int_tuple=tuple(int_list)
print(f'tuple:{int_tuple}')
int_set=set(int_list)
print(f"duplicates removed{int_set}")
int_fset=frozenset(int_set)
print(f'frozenset: {int_fset}')
int_dict={num:num**2 for num in int_fset}
print(f'dictionary :{int_dict}')

with open ('q1.txt','w')as int_db:
   int_db.write(f'list={int_dict}\n')
   int_db.write(f'list={int_fset}\n')
   print("data written to file")
with open('q1.txt','r') as int_db:
   line_fset =int_db.readline()
   line_dict=int_db.readline()
   print(line_dict)
   print(line_fset)
   
