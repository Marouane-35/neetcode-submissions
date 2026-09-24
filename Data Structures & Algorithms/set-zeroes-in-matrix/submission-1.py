class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        set_row=[None for i in range(len(matrix))]
        set_column=[None for i in range(len(matrix[0]))]
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j]==0 :
                    set_row[i]=True
                    set_column[j]=True
        for i in range(len(matrix)) :
            if set_row[i]==True :
                for j in range(len(matrix[0])) :
                    matrix[i][j]=0
        for j in range(len(matrix[0])) :
            if set_column[j]==True :
                for i in range(len(matrix)) :
                    matrix[i][j]=0




        
        