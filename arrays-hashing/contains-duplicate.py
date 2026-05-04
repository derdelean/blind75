"""
Task: Given an integer array nums, return true if any value appears more than once in the array,
otherwise return false

Check Array againt HashSet with visited elements:
Time: O(n) - Each operation takes O(1) checking/scanning array once so O(n)
Space: O(n) - HashSet creation -> Size can be up to the size of input so O(n)

Array to HashSet casting:
Time: O(n) -
Space: O(n) -

Compare neighbours (sorting first):
Time: O(n) -
Space: O(n) -

"""


from typing import List


nums = [1,2,3,4,5]

class Solution:
    def hashSet1(self, nums: List[int]) -> bool:
        visited_elements = set()
        
        for n in nums:
            if n in visited_elements:
                return True
            visited_elements.add(n)
        return False
    
    def hashSet2(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False
    
    def compareNeighbours(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
    
    def bruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False   



solution = Solution()
result = solution.bruteForce(nums)

if result:
    print("This input array has duplicates!")
else:
    print("This input array has no duplicates")
