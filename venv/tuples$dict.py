#nums=(4,8,12)
#x,y,z=nums
#print(nums)
#print(x)
#print(y)

#customers={
 #   'name' : 'Gashie',
 #   'age' : 21 ,
 #   'is_male':True

#}
#names=customers['name']
#print(names)
#years=customers['age']
#customers['is_male']=False
#print(customers)

phone=input('enter your first 3 digits : ')

phonebook={
    '1':'one',
    '2':'two' ,
    '0': 'zero',
    '3': 'zero'
}
output=''
for x in phone:
    output+=phonebook.get(x , '!')+ ' '

print(output)