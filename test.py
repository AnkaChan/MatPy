from MatPy import *
m1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
m2 = [[1, 3, 5, 7], [2, 4, 6, 8]]
m3 = [[1, 2], [3, 4], [5, 6], [7, 8]]
m4 = [[]]
mat1 = Mat(m1)
mat2 = Mat(m2)
mat3 = Mat(m3)
mat4 = Mat(m4)
print(mat1.data, '\n')
print(mat2.data)
mulm = mat1.mul(mat2)
print('multiplication:', mulm)
mulm1 = mat1.mul(mat4)
print('multiplication:', mulm1)

plusm = mat1.plus(mat3)
print('plus:', plusm)
plusm1 = mat1.plus(mat4)
print('plus:', plusm1)

scalarm = mat1.scalarMul(3)
print('scalar:', scalarm)
tansm = mat1.transpose()
print('transpose:', tansm)

mat1.show()
mat4.show()
