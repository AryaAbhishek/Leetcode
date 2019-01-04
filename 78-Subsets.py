class Solution:
    list1 = [[]]

    def forward(self, nums, temp):
        for i in range(len(nums)):
            temp1 = temp[:]
            temp1.append(nums[i])
            self.list1.append(temp1)
            if i < len(nums) - 1:
                self.forward(nums[i + 1:], temp1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.list1 = [[]]
        for i in range(len(nums)):
            temp = [nums[i]]
            self.list1.append(temp)
            if i < len(nums) - 1:
                self.forward(nums[i + 1:], temp)
        return self.list1


if __name__ == "__main__":
    s = Solution()
    a = [1,2,3]
    print(s.subsets(a))