class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        IDEA
        In this case order doesn't really matter, so how do we use binary search? After sorting, what will be important afterwards?
        Upper bound for k is the highest number in the pile, since she could eat all the other ones instantly within an hour.
        I still don't understand ngl. Like how do we get 2 with binary??
        Trying to recreate
        [1,4,3,2] -sort-> [1,2,3,4] Options for rate will be 1-4 bananas
        When are shrinking left and right though??
        //Giving up and looking at neetcode solution//
        Brute force builds up to binary search
        At most Koko can eat 1 full pile in an hour
        len(piles) <= h, since she can only eat 1 pile per hour
        Need to make sure that current h is <= h for our k
        Brute force - Start at k = 1 up until max(piles). For each pile, we'd need to know the hours it'd take to finish the pile. We can figure this out by doing ceiling(pile[i]/k), ceiling because we need to round up the hours each time.
        Runtime will be len(piles) * max(piles) -> O(n*m)
        Use binary search on the k range we get! We can start in the middle, if you can't eat the pile you know you need to focus on the right side, but if you can then you need to look at the left side to find the smallest k (with our current k still be being since it MIGHT BE that smallest k)
        runtime will be O(log(max(piles)) * piles)
        '''
        # Left and right represent boundaries of k in this case
        left = 1
        right = max(piles)
        res = max(piles)

        while left <= right:
            k = left + (right - left) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        
        return res

        