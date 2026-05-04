from typing import List

class Solution:
    def hashSet1(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
    
    
    def hashSet2(self, nums: List[int]) -> bool:
        hashSet = set(nums)

        if len(hashSet) != len(nums):
            return True
        return False
    
    def compare_neighbours(self, nums: List[int]) -> bool:
        nums.sort()

        for n in range(1, len(nums)):
            if nums[n-1] == nums[n]:
                return True
        return False
    

nums = [1,2,3,4,5,5]
result = Solution()
print(result.compare_neighbours(nums))

