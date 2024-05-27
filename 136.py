class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = dict()
        for num in nums:
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
        for key, value in check.items():
            if value == 1:
                return(key)