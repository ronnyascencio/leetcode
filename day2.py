from typing import List

""" a while loop works in this case because until the val not exist  in the list nums it will continue removing the value"""


class Solution:
    def removeElement(self, nums: List[int], val: int):
        print(f"full list: {nums}")
        while val in nums:
            nums.remove(val)


nums = [3, 2, 2, 3]
val = 3
solution = Solution()
solution.removeElement(nums=nums, val=val)
