class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        
        for x in nums:
            if x  not in count:
                count[x] = 1
            else:
                count[x]+= 1
        result = []
        for x in count:
            if count[x] > len(nums)//3:
                result.append(x)

        return result