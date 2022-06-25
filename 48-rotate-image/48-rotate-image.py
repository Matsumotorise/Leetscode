class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        # start with outter corners work through the first row
        # then inwards
        
        # 2 -> 1 layers
        # 3 -> 1 layers
        # 4 -> 2 layers
        # 5 -> 2 
        # 6 -> 3
        # 7 -> 3
        # 8 -> 4
        
        n = len(matrix)-1
        layers = (n+1) // 2
        
        for layer in range(layers):
            for i in range(0,n-2*layer):
                # four corners
                tmp = matrix[n-layer-i][layer] # bottom left

                matrix[n-layer-i][layer] = matrix[n-layer][n-layer-i] # bottom right to bottom left 
                matrix[n-layer][n-layer-i] = matrix[layer+i][n-layer] # top right to bottom right
                matrix[layer+i][n-layer] = matrix[layer][layer+i] # top left to top right
                matrix[layer][layer+i] = tmp # bottom left to top left
                

        print(matrix)

        
        