from mall.clothes import shorts
shorts()
def find_max(nums):

    mex = nums[0]

    for i in nums:

        if i > mex:
            mex = i

    largest = mex
    print(largest)

nums = [5, 12, 4, 60, 10, 20]
find_max(nums)