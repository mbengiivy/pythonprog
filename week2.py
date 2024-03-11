my_list=[]
#append 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert the value 15 to the second position
my_list.insert(1,15)

#extend my_list
second_list=[50,60,70]
my_list.extend(second_list)

#remove last element
my_list.pop()

#sort in ascending order
my_list.sort()

#find and print the index of value 30
print(my_list.index(30))
