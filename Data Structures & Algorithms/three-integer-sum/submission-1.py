class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2): #-2 since we need 3 indices total
            # If our sorted array already starts > 0, then it's impossible to get 0 at all
            if nums[i] > 0:
                break

            # Skipping duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                currTotal = nums[i] + nums[left] + nums[right]

                if currTotal < 0:
                    left += 1
                elif currTotal > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Only would need to move left because we just need to skip repeated values on ONE of the ptrs and not both 
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result