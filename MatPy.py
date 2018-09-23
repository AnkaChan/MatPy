class Mat(object):
    def __init__(self, mat0=[[]]):
        self.mat = mat0
        self.data = [mat0[i][j] for i in range(len(mat0)) for j in range(len(mat0[0]))]
        self.rows = len(mat0)
        self.cols = len(mat0[0])

    # matrix multiplication
    def mul(self, mat):
        if self.cols == mat.rows:
            # m = []
            m = [[0 for i in range(self.rows)] for j in range(mat.cols)]
            for i in range(self.rows):
                for j in range(mat.cols):
                    # m[i*mat.cols+j] = 0
                    m[i][j] = 0
                    for k in range(self.cols):
                        # m[i * mat.cols + j] += self.data[i*self.cols+k] * mat.data[k*mat.rows+j]
                        m[i][j] += self.mat[i][k] * mat.mat[k][j]
            return m
        else:
            print("The dimensions of the two matrices do not match.")

    # matrix plus
    def plus(self, mat):
        if self.rows == mat.rows and self.cols == mat.cols:
            p = [[self.mat[i][j] + mat.mat[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return p
        else:
            print("The dimensions of the two matrices do not match.")

    # matrix scalar multiplication
    def scalarMul(self, scalar):
        s = [[self.mat[i][j]*scalar for j in range(self.cols)] for i in range(self.rows)]
        return s

    def transpose(self):
        t = [[self.mat[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return t

    # show matrix
    def show(self):
        for i in self.mat:
            print(i, '\n')