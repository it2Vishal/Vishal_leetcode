class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        p1 = p2 = 0

        def get_min(p1, p2):
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    return nums1[p1], p1 + 1, p2
                else:
                    return nums2[p2], p1, p2 + 1
            elif p2 == n:
                return nums1[p1], p1 + 1, p2
            else:
                return nums2[p2], p1, p2 + 1

        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                _, p1, p2 = get_min(p1, p2)
            v1, p1, p2 = get_min(p1, p2)
            v2, p1, p2 = get_min(p1, p2)
            return (v1 + v2) / 2.0
        else:
            for _ in range((m + n) // 2):
                _, p1, p2 = get_min(p1, p2)
            val, p1, p2 = get_min(p1, p2)
            return float(val)