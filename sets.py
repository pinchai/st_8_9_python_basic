
std_list = ['ty', 'chan', 'ty', 'ra']
set_list = set(std_list)

group_name = []
for unique_name in set_list:
    count = 0
    for current in std_list:
        if current == unique_name:
            count+=1
            print(unique_name)
    group_name.append({
        'name': unique_name,
        'count': count
    })

print(group_name)



#
# std_list = {'a', 'b', 'c'}
# print(std_list[0])
# # print(type(std_list))
