class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        liste = []
        if num % 2 == 0:
            for i in range(1,(num//2)+1):
                if num % i == 0:
                    liste.append(i)
        else:
            return False
        counter = 0
        for i in liste:
            counter +=i
        print(liste)
        if counter == num:
            return True
        else:
            return False
