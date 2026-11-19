class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        m = {}
        for i in nums:
            if i in m:
                return True
            m[i]=i
        return False