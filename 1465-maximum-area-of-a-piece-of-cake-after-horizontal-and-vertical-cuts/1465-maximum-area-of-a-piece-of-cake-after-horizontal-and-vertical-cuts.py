class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        
        # Find max of derivitives
        maxH = max(y-x for y,x in zip(horizontalCuts[1:], horizontalCuts))
        maxV = max(y-x for y,x in zip(verticalCuts[1:], verticalCuts))
       
        
        return maxH*maxV % (10**9 + 7)