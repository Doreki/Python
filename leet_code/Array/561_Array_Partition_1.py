class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0;
        for i in range(0,len(nums),2) :
            sum += min(nums[i],nums[i+1])

        return sum

    def even(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i,n in enumerate(nums):

            if i % 2 == 0:
                sum +=n
        return sum


    def python(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
