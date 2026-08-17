class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        for num in nums:
            if num in count_hash:
                count_hash[num] += 1
            else:
                count_hash[num] = 1
        
        top_k = []
        top_k_cnt = []
        current_min = float('inf')
        current_min_idx = 0
        current_idx = 0
        for num, cnt in count_hash.items():
            if len(top_k) < k:
                top_k.append(num)
                top_k_cnt.append(cnt)
                if cnt < current_min:
                    current_min = cnt
                    current_min_idx = current_idx
            else:
                if cnt > current_min:
                    top_k[current_min_idx] = num
                    top_k_cnt[current_min_idx] = cnt
                    current_min = min(top_k_cnt)
                    current_min_idx = [i for i, j in enumerate(top_k_cnt) if j == current_min][0] 
            
            current_idx += 1
                
        return top_k
