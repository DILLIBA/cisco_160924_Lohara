names_list = input('enter the names(saparated with spaces): ').split()
names_set=set(names_list)
names_fset=frozenset(names_set)
names_dict={name:len(name)for name in names_fset}
print(f'original list:{names_list}')
print(f'set (no duplications):{names_set}')
print(f'forzenset:{names_fset}')
print(f'dictionary of name lengths:{names_dict}')
import json
with open('student_data.json','w')as names_db:
    json.dump(names_dict,names_db)
print('dictionary written to json file.')
with open('student_data.json','r')as names_db:
    names_dict2=json.load(names_db)
    print(f'reading from json file...\n{names_dict2}')
