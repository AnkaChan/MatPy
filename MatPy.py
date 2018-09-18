class Mat(object):
    def __init__(self, rows = 1, cols = 1, initVal = 0):
        self.data = [initVal for n in range(rows * cols)]
        self.rows = rows
        self.cols = cols

    # matrix multiplication
    def mul(self, mat):
        return Mat()

    # matrix plus
    def plus(self, mat):
        return Mat()

    # matrix scalar multiplication
    def scalarMul(self, scalar):
        return Mat()

    # show matrix
    def show(self):
        print("This fucntion will print mat")