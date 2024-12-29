class Solution():
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums2 = nums.copy()
        return [nums[nums[i]] for i in range(len(nums)) ]


if __name__ == "__main__":
    print(Solution().buildArray([0,2,1,5,3,4]))
    # 0, 1, 2, 4, 5, 3