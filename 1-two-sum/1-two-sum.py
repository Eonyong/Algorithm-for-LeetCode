class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for s in range(n - 1):
            for e in range(s + 1, n):
                if nums[s] + nums[e] == target:
                    return [s, e]