from prettytable import PrettyTable
x = PrettyTable()

x.field_names = ['ID', 'ឈ្មោះ', 'ភេទ', 'Address']
x.add_row(['1', 'Theara', 'female', 'PP'], divider=False)
x.add_row(['2', 'Vanthy', 'male', 'SR'], divider=True)
x.add_row(['3', 'Dara', 'male', 'Oddormeanchey'], divider=False)
print(x)
