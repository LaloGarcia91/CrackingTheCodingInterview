class ZeroMatrix:
    originalMatrix = [
            [1, 1, 0, 1, 0],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4]
        ]

    def __init__(self):
        self.DrawThisMatrix("----- Original Matrix -----", self.originalMatrix)
        self.LoopTheMatrixRowsAndColumns()
        self.DrawThisMatrix("----- Final Matrix columns and rows -----", self.originalMatrix)

    def LoopTheMatrixRowsAndColumns(self):
        # in here, we will save the rows index that have at least 1 zero element
        rowsIndexThatHaveZeros = []
        # in here, we will save the rows-elements index (columns index) that have at least 1 zero element
        columnsIndexThatHaveZeros = []

        for rowIndex in range(len(self.originalMatrix)):
            currentRow = self.originalMatrix[rowIndex]
            for rowElementIndex in range(len(currentRow)):
                if currentRow[rowElementIndex] == 0:
                    columnsIndexThatHaveZeros.append(rowElementIndex)
                    rowsIndexThatHaveZeros.append(rowIndex)
        self.ChangeFinalMatrixRowsElementsToZero(rowsIndexThatHaveZeros)
        self.ChangeFinalMatrixColumnsToZero(columnsIndexThatHaveZeros)

    def ChangeFinalMatrixRowsElementsToZero(self, thisRowIndexesArray):
        for rowIndex in thisRowIndexesArray:
            for rowElementIndex in range(len(self.originalMatrix[rowIndex])):
                self.originalMatrix[rowIndex][rowElementIndex] = 0

    def ChangeFinalMatrixColumnsToZero(self, thisColumnsIndexesArray):
        for rowIndex in range(len(self.originalMatrix)):
            for columnIndex in thisColumnsIndexesArray:
                self.originalMatrix[rowIndex][columnIndex] = 0

    def DrawThisMatrix(self, title, thisMatrix):
        # this methods will "beautify" the matrix in the command line.
        print(title)
        for row in thisMatrix:
            print(row)


ZeroMatrix()
