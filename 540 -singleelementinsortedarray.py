class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        if nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                return self.singleNonDuplicate(nums[:mid - 1])
            else:
                return self.singleNonDuplicate(nums[mid + 1:])
        elif nums[mid] == nums[mid + 1]:
            if mid % 2 == 0:
                return self.singleNonDuplicate(nums[mid + 2:])
            else:
                return self.singleNonDuplicate(nums[:mid])


if __name__ == "__main__":
    s = Solution()
    arr = [1,1,2,3,3,4,4,8,8]
    print(s.singleNonDuplicate(arr))