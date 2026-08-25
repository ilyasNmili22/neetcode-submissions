class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            add = [1]
            for j in range(1, i):
                print(i - 1, j - 1)    
                add += [ans[i - 1][j - 1] + ans[i - 1][j]]
            add.append(1)
            ans.append(add)
        print(ans)
        return ans[rowIndex]

'''
arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

i = 2 -> 3
1,1 + 1,2
'''