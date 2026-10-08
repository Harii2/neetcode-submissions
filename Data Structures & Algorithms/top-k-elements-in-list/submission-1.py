class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0 ) + 1 
        
        buckets = [
            [] for _ in range(len(nums) + 1)
        ]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result 
        
        return result 

        