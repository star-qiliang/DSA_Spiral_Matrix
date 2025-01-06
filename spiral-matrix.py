class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def get_sub_spira_order(min_i, max_i, min_j, max_j):
            if min_i>max_i:
                return []
            if min_j>max_j:
                return []

            res_list = []
            for j in range(min_j, max_j+1):
                # print("matrix[min_i][j]:", matrix[min_i][j])
                res_list.append(matrix[min_i][j])

            for i in range(min_i+1, max_i+1):
                # print("matrix[i][max_j]:", matrix[i][max_j])
                res_list.append(matrix[i][max_j])


            if min_i!=max_i:
                for j in range(max_j-1, min_j-1, -1):
                    # print("matrix[max_i][j]:", matrix[max_i][j])
                    res_list.append(matrix[max_i][j])

            if min_j!=max_j:
                for i in range(max_i-1, min_i, -1):
                    # print("matrix[i][min_j]:", matrix[i][min_j])
                    res_list.append(matrix[i][min_j])

            res = get_sub_spira_order(min_i+1, max_i-1, min_j+1, max_j-1)

            res_list+=res

            return res_list

        min_i = 0
        max_i = len(matrix)-1
        min_j = 0
        max_j = len(matrix[0])-1

        res_list = get_sub_spira_order(min_i, max_i, min_j, max_j)
        return res_list