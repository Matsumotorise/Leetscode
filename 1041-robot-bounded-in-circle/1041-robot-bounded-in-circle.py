class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0] 
        # XDir, YDir
        direction = 'N'
        
        directionMap = {'N':(0,1), 'W':(-1,0), 'S':(0,-1), 'E':(1, 0)}
        
        leftMap = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
        rightMap = {'N':'E', 'W':'N', 'S':'W', 'E':'S'}
        
        for s in instructions:
            if(s == 'G'):
                offset = directionMap[direction]
                pos[0] += offset[0]
                pos[1] += offset[1]
            elif(s == 'L'):
                direction = leftMap[direction]
            else:
                direction = rightMap[direction]
        if (pos[0] == 0 and pos[1] == 0) or direction != 'N':
            return True
        
        return False
        
        