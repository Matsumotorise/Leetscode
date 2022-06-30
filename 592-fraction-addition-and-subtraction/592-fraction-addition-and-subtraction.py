class Solution:
    def fractionAddition(self, expression: str) -> str:
        # parsing
        # first term could be negative
        # all terms after are fractions
        inputList = [] #(num, dem)
        
        
        data = expression.split("/")
        if len(data) == 2:
            inputList.append([data[0], data[1]])
        else:
            # First element
            inputList.append([int(data[0])])
            # Inbetween elements
            for i, s in enumerate(data[1:-1]):
                addIdx = s.find("+")
                num = div = 0
                if addIdx == -1:
                    addIdx = s.find("-")
                    prev = int(s[0:addIdx])
                    cur = -int(s[addIdx+1:])
                else:
                    prev = int(s[0:addIdx])
                    cur = int(s[addIdx+1:])
                inputList[-1].append(prev)
                inputList.append([cur])
                
            # Last element
            inputList[-1].append(int(data[-1]))

        print(inputList)

        
        # merge 2 by 2
        num, dem = inputList[0]
        
        for oNum, oDem in inputList[1:]:
            num = num *oDem + oNum*dem
            dem *= oDem
            
        if (num == 0):
            return "0/1"
        # reduce step
        gcd = math.gcd(int(num),int(dem))
        
        while gcd != 1:
            print(num,dem)
            num //= gcd
            dem //= gcd
            gcd = math.gcd(num,dem)
            
        return(f"{num}/{dem}")
            
        
        
        
        
        

            
            
                
                
                
                
            
            
            
            
        
        