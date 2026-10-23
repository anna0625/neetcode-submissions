class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# 0 1 3 0 4 
# val = 2
# k = 5

# 3, 2, 2, 3
# val = 3
# k = 2

# i = 0 -> 3 == 3 -> [3, 2, 2, 3]
# k = 0, i = 1 -> 2 != 3 -> nums[0] = nums[1] -> [2, 2, 2, 3]
# k = 1, i = 2 -> 2 != 3 -> nums[1] = nums[2] => [2, 2, 2, 3]
# k = 2, i = 3 -> 3 == 3 -> end => [2, 2, 2, 3] -> k = 2 -> [:k] -> [2, 2]