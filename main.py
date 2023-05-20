#DATA STRUCTURES AND ALGORITHMS 1
#ARRAYS

from array import *
nums=array('i',[10,20,30,40,50])

#for x in nums:
#    print(x)
print(nums[0])
print(nums[3])
#operations
nums.insert(1,21) #insert 21 at indx [1]
nums.remove(40)
y=nums.index(10) #returns the index position of value 10
nums[4]=100 #updates the value at index [4] to 100
print(nums)
print(y)


