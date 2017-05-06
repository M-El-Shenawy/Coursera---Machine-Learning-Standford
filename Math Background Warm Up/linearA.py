import numpy as np
from numpy.linalg import inv
"""
Matrix Multiplication
Ax = b
with A = [ [ [4 , -5] , [-2 , 3] ] , b = [ [13] , [-9] ].
A is 2x2 Matrix , B is 2x1 Matrix.
"""

# Matrix Declaration in numpy
A = np.array([[4, -5], [-2, 3]])
B = np.array([[13], [-9]])

# Matrix Multiplication
# A is ixj Matrix, B is jxk Matrix and The output is ixk Matrix
# PS: to multiply to Matrices use numpy dot() not multiply()!
# np.dot(A,B) = A.dot(B)
C = np.dot(A, B)
print "Multiplication of A,B:\n", C

"""
Matrix addition, subtraction, scalar multiplication
A = [ [1 , 2] , [3 , 4] ] , B = [ [5 , 6] , [7 , 8] ]
S = 3 
A is 2x2 Matrix , B is 2x2 Matrix.
"""
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
S = int(3)

# Addition of two Matrices using numpy add()
C = np.add(A, B)
print ""
print "Adding of A,B:\n", C

"""
House Prices example 
House size = [2104 , 1416 , 1534 , 852]
Having three competing hypothese: 
1) h(x) = -40+.25x 
2) h(x) = 200+.1x 
3) h(x) = -150+.04x
"""
H_Price = np.array([[1, 2104], [1, 1416], [1, 1534], [1, 852]])
Hypo = np.array([[-40, 200, -150], [.25, .1, .4]])

predict = np.dot(H_Price, Hypo)
print ""
print "Prediction:\n", predict

# Subtracting of two Matrices using numpy subtract()
C = np.subtract(A, B)
print ""
print "Subtracting of A,B:\n", C

# Scalar multiplication
C = np.multiply(S, A)
print ""
print "Scalar multiplication of S,A:\n", C

C = np.multiply(S, B)
print ""
print "Scalar multiplication of S,B:\n", C

# Identity Matrix
print ""
print "Identity Matrix[3x3]:\n", np.eye(3)

# Transpose of Matrix X.T = np.transpose(X)
X = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
print ""
print "X before Transposing:\n", X
print ""
print "X after Transposing:\n", X.T

# Inverse of Matrix
Y = np.array([[1, 2], [3, 4]])
Yinv = inv(Y)
print ""
print "Y inverse:\n", Yinv
