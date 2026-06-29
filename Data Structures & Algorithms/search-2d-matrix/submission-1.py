class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row * col - 1

        while l <=r:
            mid = l + (r - l) // 2
            rw, cl = mid//col, mid%col

            if matrix[rw][cl] < target:
                l += 1
            elif matrix[rw][cl] > target:
                r-=1
            else:
                return True
        return False


