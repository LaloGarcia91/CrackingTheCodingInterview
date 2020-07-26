class RotateMatrix:
    originalMatrixArrays = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
    ]
    originalMatrixReversed = []
    reordered90DegMatrix = []

    def __init__(self):
        self.DrawThisMatrixInCommandLine("--- Original Matrix ---", self.originalMatrixArrays)
        self.ReverseOriginalMatrix()
        self.RotateThisMatrix90Deg(self.originalMatrixReversed)
        self.DrawThisMatrixInCommandLine("--- 90 Deg Matrix ---", self.reordered90DegMatrix)

    def DrawThisMatrixInCommandLine(self, title, thisMatrix):
        print(title)
        for row in thisMatrix:
            print(row)

    def ReverseOriginalMatrix(self):
        i = len(self.originalMatrixArrays[0])-1
        while i >= 0:
            self.originalMatrixReversed.append(self.originalMatrixArrays[i])
            i -= 1

    def RotateThisMatrix90Deg(self, thisMatrix):
        for index in range(len(self.originalMatrixReversed)):
            self.reordered90DegMatrix.append([])
            for element in thisMatrix:
                self.reordered90DegMatrix[index].append(element[index])


RotateMatrix()
