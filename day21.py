#access specific element
data=[
      [1,2],
      [3,4],
      [5,6]
      ]
print(data[1][1])


#first column extrcation
marks=[
    [90,80],
    [85,75],
    [88,95]
]
print([row[0]for row in marks])


#update value
marks[0][1]=85
print(marks)


#add row
marks.append([67,34])
print(marks)


#sum of all elements
matrix1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
total=0
for row in matrix1:
    for val in row:
        total=total+val
print("Sum:",total)


#transpose of matrix
transpose=[[matrix1[j][i]for j in range(len(matrix1))]
           for i in range(len(matrix1[0]))]
print("Original matrix:",matrix1)
print("transpose matrix:",transpose)


#tic toc toe board
board=[["-" for _ in range(3)]
       for _ in range(3)]
board[1][1]='X'
for row in board:
    print(row)