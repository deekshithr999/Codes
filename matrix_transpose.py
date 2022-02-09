'''

Transpose of a matrix(n x n) is a matrix whose rows and columns are interchanged
'''
def swap(a,b):
    a,b = b,a
    return

def transpose (matrix):

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
    return



if __name__=="__main__":
    
    n=int(input())

    matrix=[]

    for i in range(n):
        matrix.append(list(map(int,input().split())))
    
    print("original: ")
    print(matrix)
    transpose(matrix)
    print("transpose: ")
    print(matrix)


