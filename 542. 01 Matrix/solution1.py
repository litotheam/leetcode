class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows_num = len(mat)
        cols_num = len(mat[0])
        # result = [[10e5] * cols_num] * rows_num
        result = [[10e5] * cols_num for i in range(rows_num)]


        for i in range(rows_num): 
            for j in range(cols_num): 
                if mat[i][j] == 0: 
                    result[i][j] = 0
                else: 
                    if i > 0:
                        result[i][j] = min(result[i][j], result[i-1][j] + 1)
                    if j > 0: 
                        result[i][j] = min(result[i][j], result[i][j-1] + 1)
        
        i = rows_num - 1
        
        while(i >= 0):
            j = cols_num - 1
            while(j >= 0):

                if i < rows_num - 1:
                    result[i][j] = min(result[i][j], result[i+1][j] + 1)
                if j < cols_num - 1:
                    result[i][j] = min(result[i][j], result[i][j+1] + 1)

                j -= 1
            i -= 1

        return result

if __name__ == '__main__':
    sol = Solution()
    mat1 = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.updateMatrix(mat1))
    mat2 = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
    print(sol.updateMatrix(mat2))