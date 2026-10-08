class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)

        prefix[0] = height[0]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i])
        
        suffix[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        # print(prefix, suffix)
        water_trapped = 0 

        for i in range(len(height)):
            curr_height = min(
                prefix[i], suffix[i]
            )
            
            water_trapped += abs(
                curr_height - height[i]
            )
        
        return water_trapped
