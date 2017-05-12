% Matrix declaration 
A = [4 -5 ; -2 3]; 
B = [13 ; -9]; 

% Matrix Multiplication 'Dot product'
C = A*B 

% Matrix Element wise Multiplication 'Element-by-element multiplication' 
C = A .* B 

% Matrix Addition 
A1 = [1 2 ; 3 4];
B1 = [5 6 ; 7 8];
C1 = A1+B1 

% Matrix Subtraction 
C1 = A1-B1

% Scaler multiplication 
S = 5 
C1 =  S * A1 

% Identiy Matrix 
I = eye(3)

% Matrix Transpose 
T = A1' % or A1.'

% Matrix Inverse 
invA = pinv(A) %Pseudo inverse  

% Multiplying Original matrix A by it's inverse by A will give the original Matrix A
A * invA * A  