class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sozluk = dict()
        for i in nums:
            if i in sozluk:
                sozluk[i] += 1
            else:
                sozluk[i] = 1
        for val in sozluk.values():
            if val != 1:
                return True