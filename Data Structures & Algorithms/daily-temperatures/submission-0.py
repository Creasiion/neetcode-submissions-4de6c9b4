class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        UNDERSTANDING: the element value represents the # of days it'll take to see a warmer day compared to that element

        IDEA: If we use a monotonic stack, we can organize it descending? When we get a higher value, then we can being popping. The next day we'll see that's hotter would be # popped + 1

        PSEUDOCODE
        for i in range len(arr)

            while stack and arr[stack[-1]] < arr[i]:
                prev_index = stack.pop()
                result[prev_index] += 1
                
            stack.append(i)

        '''
        stack = [] #will store INDEXES of the sorted days
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                result[prev_index] += i-prev_index
            stack.append(i)

        return result


