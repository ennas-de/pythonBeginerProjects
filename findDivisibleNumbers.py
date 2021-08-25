my_range = int(input("Enter upper number: "))
my_list = list()
for i in range(my_range):
    my_list.append(i)

result = list(filter(lambda x: (x%13 == 0), my_list))

print(result)