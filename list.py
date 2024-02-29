from prettytable import PrettyTable
x = PrettyTable()

step = 1
std_list = []
while step <= 3:
    name = input('Enter name: ')
    gender = input('Enter gender: ')
    std = {
        'name': name,
        'gender': gender
    }
    std_list.append(std)
    step+=1

x.field_names = ['ID', 'ឈ្មោះ', 'ភេទ', 'Address']
x.add_row(['1', 'Theara', 'female', 'PP'], divider=False)
x.add_row(['2', 'Vanthy', 'male', 'SR'], divider=True)
x.add_row(['3', 'Dara', 'male', 'Oddormeanchey'], divider=False)
print(x)
