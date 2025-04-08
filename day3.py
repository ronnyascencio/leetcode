"""

Remove Duplicates from Sorted Array

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(f"result of the list default items: {nums}")
        new_nums = set(nums)
        """ set() removes any repetitive  item  converting the list in a dictionary need to be transformed to get a list back"""
        nums.clear()
        for i in (
            new_nums
        ):  # reviewing each item of the dict  converted from the list with set()
            nums.append(
                i
            )  # adding the item in to the list  i cleared before  to convert the items in the dict  to a list
        nums.sort()  # sorting in orther the items
        print(f"result of the list with any repetitive item: {nums}")
        return len(nums)


nums = [1, 1, 2]
result = Solution()
print(
    f"this is the final result with the count of items inside the list: {result.removeDuplicates(nums=nums)}"
)
