import numpy as np

def det(matrix):
    firstRow = matrix[0]

    if len(firstRow) == 1:
        return firstRow[0]

    # 2x2
    if len(firstRow) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    ans = 0

    for i in range(len(firstRow)):
        sign = -1 if i % 2 == 1 else 1

        minor = []
        for row in range(1, len(matrix)):
            minorRow = []
 
            for col in range(len(matrix[0])):   
                if col == i:
                    continue

                minorRow.append(matrix[row][col])

            minor.append(minorRow)
            
        ans += sign * firstRow[i] * det(np.array(minor))

    return ans

M = np.array([[1, 2, 3], [0, 5, 6], [0, 0, 9]])
print(M)
print(det(M))
print(np.linalg.det(M))

def maxDet(dim):
    count = 0
    currentMax = -np.inf

    return count

print(maxDet(2))