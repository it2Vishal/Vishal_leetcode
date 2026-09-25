class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0
        prev, curr = 0, 0
        
        # Advance pointers step-by-step to the middle point
        for _ in range((m + n) // 2 + 1):
            prev = curr
            if p1 < m and (p2 >= n or nums1[p1] < nums2[p2]):
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1
                
        # If total length is odd, return middle element
        if (m + n) % 2 != 0:
            return float(curr)
            
        # If total length is even, return average of the two middle elements
        return (prev + curr) / 2.0