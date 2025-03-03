class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:

        # 1.      
        less = []
        p = []
        greater = []

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                p.append(n)
        
        return less + p + greater # concatenation of arrays

        #2. without 2 extra memory, two pointer approach
        i, j = 0, len(nums)-1 # 2 pointers
        i2, j2 = 0, len(nums) - 1 # these will tell us the insertion positions of res array
        res = [0] * len(nums) # for same size as input array

        while i < len(nums): # or j>=0 any can be true
            if nums[i] < pivot:
                res[i2] = nums[i] # at i2 set nums[i]
                i2 += 1
            if nums[j] > pivot:
                res[j2] = nums[j]
                j2 -= 1
            i, j = i+1, j-1

        while i2 <= j2: # for pivot elements 
            res[i2] = res[j2] = pivot
            i2, j2 = i2+1, j2-1
        return res