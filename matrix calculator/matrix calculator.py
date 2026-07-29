print("__"*77)
print("")
print("                                                                MATRIX CALCULATOR")
print("")
print("__"*77)
print("")
print("""                                         YOU NEED TO ENTER OPTION BETWEEN 1-10 TO PERFORM FOLLOWING ACTIONS
                                                                1. Matrix Addition(+)
                                                                2. Matrix Subtraction(-)
                                                                3. Matrix Multiplication(X)
                                                                4. Transpose of a Matrix
                                                                5. Determinant of a Matrix
                                                                6. Inverse of Matrix
                                                                7. Identity Matrix Check
                                                                8. Matrix Statistics (sum, max, min)
                                                                9. Save Calculation History to a File
                                                                10. View Previous Calculations
                                                                11. Clear History
                                                                12. Exit
""")
def input_main(name):
    print(name)
    rows = int(input("ENTER THE NUMBER OF ROWS:"))  #taking number of rows from user
    column = int(input("ENTER THE NUMBER OF COLUMNS: "))    #taking number of column from user
    print("YOU WANT SOLUTION OF ",rows,"X",column)
    matrix=[]
    print("ENTER THE ELEMENTS OF MATIX")
    for i in range(rows):
        row=[]
        for j in range(column):
            value=float(input(f"Enter the the element {i+1}{j+1}"))
            row.append(value)
        matrix.append(row)
    return matrix
matrix_a=input_main("MATRIX A")
matrix_b=input_main("MATRIX B")
def additon_matrix(matrix_a,matrix_b):
def display_matrix(matrix,name):
    print("YOUR",name,"is:")
    for row in matrix:
        print(row)

