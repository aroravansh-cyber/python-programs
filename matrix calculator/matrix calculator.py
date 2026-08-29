import json
import os

HISTORY_FILE = "matrix_history.json"


# -------------------- DISPLAY --------------------

print("__" * 77)
print("")
print("                              MATRIX CALCULATOR")
print("")
print("__" * 77)
print("")

print("""
YOU NEED TO ENTER AN OPTION BETWEEN 1-12 TO PERFORM THE FOLLOWING ACTIONS

1. Matrix Addition (+)
2. Matrix Subtraction (-)
3. Matrix Multiplication (X)
4. Transpose of a Matrix
5. Determinant of a Matrix
6. Inverse of a Matrix
7. Identity Matrix Check
8. Matrix Statistics (sum, max, min)
9. Save Calculation History to a File
10. View Previous Calculations
11. Clear History
12. Exit
""")


# -------------------- INPUT MATRIX --------------------

def input_main(name):
    print("\n", name)

    while True:
        try:
            rows = int(input("ENTER THE NUMBER OF ROWS: "))
            columns = int(input("ENTER THE NUMBER OF COLUMNS: "))

            if rows <= 0 or columns <= 0:
                print("Rows and columns must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter valid numbers.")

    print("YOU WANT SOLUTION OF", rows, "X", columns)

    matrix = []

    print("ENTER THE ELEMENTS OF MATRIX")

    for i in range(rows):
        row = []

        for j in range(columns):
            while True:
                try:
                    value = float(
                        input(f"Enter element [{i + 1}][{j + 1}]: ")
                    )
                    row.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number.")

        matrix.append(row)

    return matrix


# -------------------- DISPLAY MATRIX --------------------

def display_matrix(matrix, name="MATRIX"):
    print("\nYOUR", name, "IS:")

    for row in matrix:
        print("  ".join(f"{value:g}" for value in row))


# -------------------- ADDITION --------------------

def addition_matrix(matrix_a, matrix_b):

    if len(matrix_a) != len(matrix_b):
        return None

    if len(matrix_a[0]) != len(matrix_b[0]):
        return None

    result = []

    for i in range(len(matrix_a)):
        row = []

        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])

        result.append(row)

    return result


# -------------------- SUBTRACTION --------------------

def subtraction_matrix(matrix_a, matrix_b):

    if len(matrix_a) != len(matrix_b):
        return None

    if len(matrix_a[0]) != len(matrix_b[0]):
        return None

    result = []

    for i in range(len(matrix_a)):
        row = []

        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] - matrix_b[i][j])

        result.append(row)

    return result


# -------------------- MULTIPLICATION --------------------

def multiplication_matrix(matrix_a, matrix_b):

    if len(matrix_a[0]) != len(matrix_b):
        return None

    result = []

    rows_a = len(matrix_a)
    columns_b = len(matrix_b[0])

    for i in range(rows_a):
        row = []

        for j in range(columns_b):

            total = 0

            for k in range(len(matrix_b)):
                total += matrix_a[i][k] * matrix_b[k][j]

            row.append(total)

        result.append(row)

    return result


# -------------------- TRANSPOSE --------------------

def transpose_matrix(matrix):

    rows = len(matrix)
    columns = len(matrix[0])

    result = []

    for j in range(columns):

        row = []

        for i in range(rows):
            row.append(matrix[i][j])

        result.append(row)

    return result


# -------------------- DETERMINANT --------------------

def determinant(matrix):

    n = len(matrix)

    if n != len(matrix[0]):
        return None

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    for column in range(n):

        minor = []

        for i in range(1, n):

            row = []

            for j in range(n):

                if j != column:
                    row.append(matrix[i][j])

            minor.append(row)

        sign = (-1) ** column

        det += sign * matrix[0][column] * determinant(minor)

    return det


# -------------------- INVERSE --------------------

def inverse_matrix(matrix):

    n = len(matrix)

    if n != len(matrix[0]):
        return None

    det = determinant(matrix)

    if abs(det) < 1e-10:
        return None

    # Create augmented matrix [A | I]

    augmented = []

    for i in range(n):

        row = []

        for j in range(n):
            row.append(matrix[i][j])

        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)

        augmented.append(row)

    # Gauss-Jordan elimination

    for i in range(n):

        pivot = augmented[i][i]

        if abs(pivot) < 1e-10:

            for k in range(i + 1, n):

                if abs(augmented[k][i]) > 1e-10:
                    augmented[i], augmented[k] = (
                        augmented[k],
                        augmented[i]
                    )
                    pivot = augmented[i][i]
                    break

        if abs(pivot) < 1e-10:
            return None

        for j in range(2 * n):
            augmented[i][j] /= pivot

        for k in range(n):

            if k != i:

                factor = augmented[k][i]

                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]

    inverse = []

    for i in range(n):
        inverse.append(augmented[i][n:])

    return inverse


# -------------------- IDENTITY MATRIX CHECK --------------------

def is_identity(matrix):

    rows = len(matrix)
    columns = len(matrix[0])

    if rows != columns:
        return False

    for i in range(rows):

        for j in range(columns):

            if i == j:

                if matrix[i][j] != 1:
                    return False

            else:

                if matrix[i][j] != 0:
                    return False

    return True


# -------------------- STATISTICS --------------------

def matrix_statistics(matrix):

    values = []

    for row in matrix:
        for value in row:
            values.append(value)

    return {
        "sum": sum(values),
        "max": max(values),
        "min": min(values)
    }


# -------------------- HISTORY --------------------

def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    except:
        return []


history = load_history()


def add_history(operation, result):

    history.append({
        "operation": operation,
        "result": result
    })


def save_history():

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

    print("Calculation history saved successfully.")


def view_history():

    if not history:
        print("No previous calculations found.")
        return

    print("\nPREVIOUS CALCULATIONS")

    for i, item in enumerate(history, start=1):

        print("\nCalculation", i)
        print("Operation:", item["operation"])
        print("Result:", item["result"])


def clear_history():

    history.clear()

    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

    print("History cleared successfully.")


# -------------------- MAIN PROGRAM --------------------

while True:

    print("\n" + "=" * 60)
    print("MATRIX CALCULATOR MENU")
    print("=" * 60)

    print("""
1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
4. Transpose
5. Determinant
6. Inverse
7. Identity Matrix Check
8. Matrix Statistics
9. Save Calculation History
10. View Previous Calculations
11. Clear History
12. Exit
""")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))

    except ValueError:
        print("Please enter a number between 1 and 12.")
        continue


    # Addition

    if choice == 1:

        matrix_a = input_main("MATRIX A")
        matrix_b = input_main("MATRIX B")

        result = addition_matrix(matrix_a, matrix_b)

        if result is None:
            print("Both matrices must have the same dimensions.")

        else:
            display_matrix(result, "ADDITION RESULT")
            add_history("Matrix Addition", result)


    # Subtraction

    elif choice == 2:

        matrix_a = input_main("MATRIX A")
        matrix_b = input_main("MATRIX B")

        result = subtraction_matrix(matrix_a, matrix_b)

        if result is None:
            print("Both matrices must have the same dimensions.")

        else:
            display_matrix(result, "SUBTRACTION RESULT")
            add_history("Matrix Subtraction", result)


    # Multiplication

    elif choice == 3:

        matrix_a = input_main("MATRIX A")
        matrix_b = input_main("MATRIX B")

        result = multiplication_matrix(matrix_a, matrix_b)

        if result is None:
            print(
                "Matrix multiplication is not possible."
                " Columns of A must equal rows of B."
            )

        else:
            display_matrix(result, "MULTIPLICATION RESULT")
            add_history("Matrix Multiplication", result)


    # Transpose

    elif choice == 4:

        matrix = input_main("MATRIX")

        result = transpose_matrix(matrix)

        display_matrix(result, "TRANSPOSE")
        add_history("Matrix Transpose", result)


    # Determinant

    elif choice == 5:

        matrix = input_main("MATRIX")

        result = determinant(matrix)

        if result is None:
            print("Determinant is only possible for a square matrix.")

        else:
            print("\nDETERMINANT =", result)
            add_history("Determinant", result)


    # Inverse

    elif choice == 6:

        matrix = input_main("MATRIX")

        result = inverse_matrix(matrix)

        if result is None:
            print("Matrix does not have an inverse.")

        else:
            display_matrix(result, "INVERSE")
            add_history("Matrix Inverse", result)


    # Identity Check

    elif choice == 7:

        matrix = input_main("MATRIX")

        result = is_identity(matrix)

        if result:
            print("The matrix IS an identity matrix.")

        else:
            print("The matrix IS NOT an identity matrix.")

        add_history("Identity Matrix Check", result)


    # Statistics

    elif choice == 8:

        matrix = input_main("MATRIX")

        result = matrix_statistics(matrix)

        print("\nMATRIX STATISTICS")
        print("SUM:", result["sum"])
        print("MAX:", result["max"])
        print("MIN:", result["min"])

        add_history("Matrix Statistics", result)


    # Save History

    elif choice == 9:

        save_history()


    # View History

    elif choice == 10:

        view_history()


    # Clear History

    elif choice == 11:

        clear_history()


    # Exit

    elif choice == 12:

        print("Thank you for using Matrix Calculator.")
        break


    else:

        print("Invalid choice. Please select 1-12.")
