class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        i, j = 0, 0 # pointers at 0 index of nums1 and nums2 arrays
        res = [] # resulting array

        while i < len(nums1) and j < len(nums2): # checking if i and j are in bounce and do some comparisons
            if nums1[i][0] < nums2[j][0]: # [0] is index for id
                res.append(nums1[i]) # appending whole [id][val]
                i += 1

            elif nums2[j][0] < nums1[i][0]:
                res.append(nums2[j])
                j += 1
            else: # both are equal 
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i, j = i + 1, j+1
        while i < len(nums1): # checking nums1 i is in bounce
            res.append(nums1[i]) # appending all thte nums1 
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        
        return res
                       