
names=['Gashi','Jon','Swey','Tino']
print(names[0])
print(names[2:])
print(names[-1])
names[0]='Gashy'
print(names)

nums=[8,10,10,20,12,5,3,20]
#removing duplicates
nums2=[]
for x in nums :
    if x  not in nums2:
        nums2.append(x)

print(nums2)
max=nums[0]
nums.sort()
print(nums)
nums.pop()
nums.append(50)
print(nums.index(3))
nums.append(100)
nums.sort()
nums.reverse()
nums.insert(0,1000)
print(nums)
#for i in  nums :
#    if i > max :
#        max=i
#print(f'the max number is : {max}')
#largest=max(nums)
#print(largest)