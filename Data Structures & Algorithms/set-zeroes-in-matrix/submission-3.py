class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        set_row=set()
        set_column=set()
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j]==0 :
                    set_row.add(i)
                    set_column.add(j)
        for i in set_row :
            for j in range(len(matrix[0])) :
                matrix[i][j]=0
        for j in set_column :
            for i in range(len(matrix)) :
                matrix[i][j]=0




        
        