words_list=input('enter the elements(sparatede by space)').split()
words_tuple=tuple(words_list)
print(f'list={words_list}')
print(f'list={words_tuple}')

with open('qn01_data.txt','w')as data_file:
    data_file.write(f'list={words_list}\n')
    data_file.write(f'list={words_tuple}\n')
print('data written to file')
with open('qn01_data.txt','r')as data_file:
    line_list = data_file.readline()
    line_tuple = data_file.readline()
    print(line_list)
    print(line_tuple)