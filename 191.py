class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for index, element in enumerate(bin(n)):
            if index >= 2:
                element = int(element)
                counter +=element
        return counter
                