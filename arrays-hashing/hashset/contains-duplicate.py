"""
Task: Given an integer array nums, return true if any value appears more than once in the array, 
otherwise return false

Time: O(n) - Each operation takes O(1) checking/scanning array once so O(n)
Space: O(n) - HashSet creation -> Size can be up to the size of input so O(n)

Check Array againt HashSet with visited elements
"""


from typing import List


nums = [1,2,3,4,1]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited_elements = set()
        
        for n in nums:
            if n in visited_elements:
                return True
            visited_elements.add(n)
        return False


solution = Solution()
result = solution.containsDuplicate(nums)

if result:
    print("This input array has duplicates!")
else:
    print("This input array has no duplicates")
