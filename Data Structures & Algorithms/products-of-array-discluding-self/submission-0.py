class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        zero_found = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                product_all *= nums[i]
            else:
                zero_found += 1
            if zero_found == 2:
                return [0] * len(nums)
        
        res = []
    
        for i in range(0, len(nums)):
            if nums[i] == 0:
                res.append(product_all)
            else:
                res.append(int((product_all / nums[i]) * (1 - zero_found)))
        return res