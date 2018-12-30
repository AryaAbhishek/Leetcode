class Solution(object):
    # def findleft(self, nums, target, start):
    #     if len(nums)==1:
    #         return start+1
    #     mid = len(nums)//2
    #     if nums[mid] == target:
    #         if nums[mid-1] == target:
    #             return self.findleft(nums[:mid],target, start+mid-len(nums))
    #         else:
    #             return start+mid-len(nums)

    def search(self, nums, target, start):
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [start, start]
            else:
                return [-1, -1]
        mid = len(nums) // 2
        if nums[mid] == target:
            # i = self.find(nums[:mid], target, mid)
            # j = self.find(nums[mid+1:],target,mid+1)
            i = mid
            j = mid
            while i > 0:
                if nums[i - 1] == target:
                    i -= 1
                else:
                    break
            while j < len(nums) - 1:
                if nums[j + 1] == target:
                    j += 1
                else:
                    break
            return [i + start, j + start]
        else:
            if nums[mid] < target:
                return self.search(nums[mid + 1:], target, start + mid + 1)
            else:
                return self.search(nums[:mid], target, start)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.search(nums, target, 0)


if __name__ == "__main__":
    s = Solution()
    arr = [5,7,7,8,8,10]
    target = 8
    print(s.searchRange(arr, target))