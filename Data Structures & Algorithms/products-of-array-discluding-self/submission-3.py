class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) attempt
        # E.x.1 Using 48 -> 2 * 4 * 6
        # Is it possible to use some kind of preprocessing?
        # Brute force idea is 2-ptr kind of approach, where
        # We keep track of the current index, and with another ptr
        # Go multiply the values together - Would be O(n^2) though
        # Maybe preprocessing wise we multiply all values together already, then find a way to get rid of element(i) from the result
        # Edge Case: 0's in array - maybe store total product and
        # total product EXCLUDING 0s, if more than 1 0 answer will 
        # always be 0
        totalProd = 1
        zeroCounter = 0
        res = []
        #Preprocessing
        for num in nums:
            if num == 0:
                zeroCounter += 1
            else:
                totalProd *= num
        #Finding answer
        for num in nums:
            if zeroCounter > 1 : # ALL answers will be 0
                res.append(0)
            elif zeroCounter == 1: # Every answer but when num == 0 will be 0
                if num == 0:
                    res.append(totalProd)
                else:
                    res.append(0)
            else:
                res.append(totalProd//num)
    
        return res



        