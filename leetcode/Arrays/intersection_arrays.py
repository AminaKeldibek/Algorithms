class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inters_hash = dict()
        inters = []

        for n in nums1:
            if n not in inters_hash:
                inters_hash[n] = 1

        for n in nums2:
            if n in inters_hash:
                inters_hash[n] += 1

        for key, val in inters_hash.iteritems():
            if val > 1:
                inters.append(key)

        return inters



        
