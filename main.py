mat1 = [[1, 2, 3], [4, 5, 6]]
mat2 = [[7, 8], [9, 10], [11, 12]]

class Matrix:
    
    listOfLists : list

    def __init__(self, numberOfRows, numberOfCols):
        self.listOfLists = []
        rowList = [] 
        for _ in range(numberOfCols):
            rowList.append(0)
        for _ in range(numberOfRows):
            self.listOfLists.append(rowList[:])
    
    def numRows(self):
        return len(self.listOfLists)

    def numCols(self):
        return len(self.listOfLists[0])

       
    def littlePrettierPrinter(self):
        for row in self.listOfLists:
            print(row)
        print("\n")

    def setValue(self, row, col, value):
        if row >= self.numRows() or col >= self.numCols():
            print("Make sure the rows/cols are in range")
            return
        self.listOfLists[row][col] = value

    def getValue(self, row, col):
        if row >= self.numRows() or col >= self.numCols():
            print("Make sure the rows/cols are in range")
            return
        return self.listOfLists[row][col]

    def scalarMultiplication(self, scalar):
        for row in range(len(self.listOfLists)):
            for col in range(len(self.listOfLists[0])):
                self.listOfLists[row][col] = scalar * self.listOfLists[row][col]

    def addTwoMatrices(self, matrix2):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                sumOfVals = self.getValue(i, j) + matrix2.getValue(i, j)
                self.setValue(i, j, sumOfVals)

    def dotProduct(self, matrix2):
        resultRows = self.numRows()
        resultCols = matrix2.numCols()
        
        resultMatrix = Matrix(resultRows, resultCols)

        for row in range(resultRows):
            for col in range(resultCols):
                matrix1Row = row
                matrix2Col = col
                sum = 0
                for i in range(self.numCols()):
                    sum = sum + self.getValue(matrix1Row, i) * matrix2.getValue(i, matrix2Col)
                               
                resultMatrix.setValue(row, col, sum)
        return resultMatrix

class Vector(Matrix):
    def __init__(self, direction, length):
        if direction == 'horizontal':
            super().__init__(1, length)
        elif direction == 'vertical':
            super().__init__(length, 1)
        



a = Matrix(3, 3)
a.setValue(0, 0, 2)
a.setValue(1, 1, 2)
a.setValue(2, 2, 2)
a.littlePrettierPrinter()
b = Matrix(3, 1)
b.setValue(2, 0, 10)
b.littlePrettierPrinter()
c = a.dotProduct(b)
c.littlePrettierPrinter()

vec1 = Vector('horizontal', 5)
vec1.setValue(0, 3, 5)
vec2 = Vector('horizontal', 5)
vec2.setValue(0, 3, 6)
print("Printing vec1: ")
vec1.littlePrettierPrinter()
print("Printing vec2: ")
vec2.littlePrettierPrinter()

vec1.addTwoMatrices(vec2)
print("Printing vec1 after addition: ")
vec1.littlePrettierPrinter()

