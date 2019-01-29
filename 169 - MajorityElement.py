class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dict1 = {}
        # if nums is None:
        #     return 0
        # for i in nums:
        #     if i not in dict1:
        #         dict1[i] = 1
        #     dict1[i] += 1
        # val = 0
        # for i in dict1:
        #     if val == 0:
        #         val = i
        #     if dict1[i]>dict1[val]:
        #         val = i
        # return val

        count = 0
        val = None
        for i in nums:
            if count == 0:
                val = i
            count += (1 if i == val else -1)
        return val

if __name__ == "__main__":
    a = [3,2,3]
    s= Solution()
    print(s.majorityElement(a))