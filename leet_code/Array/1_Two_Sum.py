from _ast import List


class Solution:
    def brute_force(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j];

    def with_in(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

    def first_minus1(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums) :
            nums_map[num] = i

        for i, num in enumerate(nums) :
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    def first_minus2(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
