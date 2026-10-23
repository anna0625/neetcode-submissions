class Solution:

    def __init__(self):
        self.max_number = 0
        self.current_streak = 0

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        for current_number in nums:
            if current_number == 1:
                self.current_streak += 1
                self.max_number = max(self.max_number, self.current_streak)
            elif current_number == 0:
                self.current_streak = 0
        return self.max_number