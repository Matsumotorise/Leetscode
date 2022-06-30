class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        # dfs problem
        # Either take or don't take coin any further
        
        cache = {}

        def dfs(i=0, amt=0):
            if amt == amount:
                return 1
            elif amt > amount:
                return 0
            elif (i,amt) in cache:
                return cache[(i,amt)]
                
            
            
            s = 0
            if i+1 < len(coins):
                s += dfs(i+1, amt)
            s += dfs(i, amt + coins[i])
            
            cache[(i,amt)] = s
            return s
            
            
        return dfs()
        
        
        
        