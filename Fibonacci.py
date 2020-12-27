import numpy as np
import time
def Fibonacci_recursive(n):
    if n == 0: return 0
    if n==1 or n==2 : return 1
    
    return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)

def Fibonacci_dynamic(n):
    FibonacciTable = [-1]*(n+1)
    
    if n ==0 or n == 1:
        return n
    FibonacciTable[0] = 0
    FibonacciTable[1] = 1
    
    for i in range(2,n+1):
        FibonacciTable[i] = FibonacciTable[i-1] + FibonacciTable[i-2]
    Result = FibonacciTable[n]
    return Result

def Fibonacci_matrix(n):
    def Matrixpower(A,n):
        if n>1:
            A = Matrixpower(A,n//2)
            A = np.dot(A,A)
            if n%2 == 1:
                B = np.array([[1,1],[1,0]])
                A = np.dot(A,B)
        return A
    
    A = np.array([[1,1],[1,0]])
    return Matrixpower(A,n)[0,1]
   
start = time.time()
print("recursive 2^n")
print(Fibonacci_recursive(40))
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간        

start = time.time()
print("recursive n")
print(Fibonacci_dynamic(40))
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

start = time.time()
print("recursive log n")
print(Fibonacci_matrix(40))
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간