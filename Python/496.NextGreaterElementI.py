class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for n in nums2:
            while stack and stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)

        return [dic.get(n, -1) for n in nums1]