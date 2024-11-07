from typing import List
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           if remaining in seen:
               return [seen[remaining], i]
           else:
               seen[value] = i   
               
sl = Solution()

nums = [3, 2, 4]
target = 6
result = sl.twoSum(nums, target)

print(result)  