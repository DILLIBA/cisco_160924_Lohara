num_list=[int(num) for num in input('enter the integers (space)').split()]
num_dict={num:len(num) for num in num_list}

with open('q21.txt','w') as q21_db:
    q21_db.write(f'list: {num_dict}/n')
with open('q21.txt','r') as q21_db:
    line_dict=q21_db.readline()
    print(f'dictinary: {line_dict}')


