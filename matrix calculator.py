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
    rows = int(input("ENTER THE NUMBER OF ROWS:"))  #taking number of rows from user
    column = int(input("ENTER THE NUMBER OF COLUMNS: "))    #taking number of column from user
    print("YOU WANT SOLUTION OF ",rows,"X",column)
    