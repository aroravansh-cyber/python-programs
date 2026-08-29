import random

# =========================
# QUIZ QUESTIONS
# =========================

beginner = [
    {
        "question": "What is the correct file extension for Python?",
        "options": ["A. .java", "B. .py", "C. .cpp", "D. .html"],
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. show()", "B. display()", "C. print()", "D. output()"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!-- -->", "D. **"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used for a condition?",
        "options": ["A. if", "B. check", "C. condition", "D. when"],
        "answer": "A"
    },
    {
        "question": "Which data type stores whole numbers?",
        "options": ["A. float", "B. str", "C. int", "D. bool"],
        "answer": "C"
    },
    {
        "question": "Which function takes input from the user?",
        "options": ["A. get()", "B. input()", "C. scan()", "D. read()"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for multiplication?",
        "options": ["A. x", "B. *", "C. #", "D. %"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to repeat a loop?",
        "options": ["A. for", "B. repeat", "C. loop", "D. again"],
        "answer": "A"
    },
    {
        "question": "Which value represents True or False?",
        "options": ["A. int", "B. bool", "C. str", "D. float"],
        "answer": "B"
    },
    {
        "question": "Which brackets are used to create a list?",
        "options": ["A. ()", "B. {}", "C. []", "D. <>"],
        "answer": "C"
    }
]


intermediate = [
    {
        "question": "Which keyword is used to create a function?",
        "options": ["A. function", "B. def", "C. fun", "D. create"],
        "answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["A. add()", "B. append()", "C. insertItem()", "D. push()"],
        "answer": "B"
    },
    {
        "question": "What does len() return?",
        "options": ["A. Data type", "B. Length", "C. Index", "D. Memory"],
        "answer": "B"
    },
    {
        "question": "Which loop is commonly used with a list?",
        "options": ["A. for", "B. switch", "C. case", "D. goto"],
        "answer": "A"
    },
    {
        "question": "Which operator checks equality?",
        "options": ["A. =", "B. ==", "C. !=", "D. ==="],
        "answer": "B"
    },
    {
        "question": "What does range(5) produce?",
        "options": ["A. 1 to 5", "B. 0 to 5", "C. 0 to 4", "D. 1 to 4"],
        "answer": "C"
    },
    {
        "question": "Which keyword stops a loop?",
        "options": ["A. stop", "B. exit", "C. break", "D. end"],
        "answer": "C"
    },
    {
        "question": "Which keyword skips the current loop iteration?",
        "options": ["A. skip", "B. continue", "C. pass", "D. next"],
        "answer": "B"
    },
    {
        "question": "Which type stores decimal numbers?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "B"
    },
    {
        "question": "Which method converts text to lowercase?",
        "options": ["A. lower()", "B. small()", "C. lowercase()", "D. down()"],
        "answer": "A"
    },
    {
        "question": "Which operator means 'not equal'?",
        "options": ["A. <>", "B. !=", "C. =!", "D. not="],
        "answer": "B"
    },
    {
        "question": "What does input() normally return?",
        "options": ["A. int", "B. float", "C. string", "D. bool"],
        "answer": "C"
    },
    {
        "question": "Which keyword handles another condition?",
        "options": ["A. else if", "B. elseif", "C. elif", "D. otherwise"],
        "answer": "C"
    },
    {
        "question": "Which collection does not allow duplicate values?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. String"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for exponentiation?",
        "options": ["A. ^", "B. **", "C. ^^", "D. //"],
        "answer": "B"
    },
    {
        "question": "What does // perform?",
        "options": ["A. Normal division", "B. Floor division", "C. Multiplication", "D. Modulus"],
        "answer": "B"
    },
    {
        "question": "Which function converts a value to an integer?",
        "options": ["A. integer()", "B. int()", "C. number()", "D. convert()"],
        "answer": "B"
    },
    {
        "question": "Which function converts a value to a string?",
        "options": ["A. string()", "B. text()", "C. str()", "D. convert()"],
        "answer": "C"
    },
    {
        "question": "Which keyword imports a module?",
        "options": ["A. include", "B. import", "C. using", "D. module"],
        "answer": "B"
    },
    {
        "question": "Which function returns the largest value?",
        "options": ["A. large()", "B. maximum()", "C. max()", "D. high()"],
        "answer": "C"
    },
    {
        "question": "Which function returns the smallest value?",
        "options": ["A. min()", "B. small()", "C. lowest()", "D. minimum()"],
        "answer": "A"
    },
    {
        "question": "What does list.sort() do?",
        "options": ["A. Deletes a list", "B. Sorts the list", "C. Copies the list", "D. Reverses the list"],
        "answer": "B"
    },
    {
        "question": "Which method removes an item from a list?",
        "options": ["A. delete()", "B. remove()", "C. erase()", "D. clearItem()"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. Boolean", "B. Integer", "C. String", "D. Float"],
        "answer": "A"
    }
]


advanced = [
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. catch", "B. try", "C. error", "D. exception"],
        "answer": "B"
    },
    {
        "question": "Which block handles an exception?",
        "options": ["A. catch", "B. except", "C. error", "D. handle"],
        "answer": "B"
    },
    {
        "question": "What is a lambda function?",
        "options": [
            "A. A loop",
            "B. Anonymous function",
            "C. Class",
            "D. Module"
        ],
        "answer": "B"
    },
    {
        "question": "Which keyword creates a class?",
        "options": ["A. object", "B. class", "C. struct", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which function returns the type of an object?",
        "options": ["A. typeof()", "B. type()", "C. object_type()", "D. datatype()"],
        "answer": "B"
    },
    {
        "question": "Which concept allows a class to inherit another class?",
        "options": ["A. Encapsulation", "B. Inheritance", "C. Iteration", "D. Compilation"],
        "answer": "B"
    },
    {
        "question": "What is PEP 8?",
        "options": [
            "A. Python security tool",
            "B. Python style guide",
            "C. Python compiler",
            "D. Python database"
        ],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a generator?",
        "options": ["A. generate", "B. yield", "C. generator", "D. return"]
        ,
        "answer": "B"
    },
    {
        "question": "What does *args allow?",
        "options": [
            "A. Multiple positional arguments",
            "B. Multiple files",
            "C. Multiple classes",
            "D. Multiple modules"
        ],
        "answer": "A"
    },
    {
        "question": "What does **kwargs allow?",
        "options": [
            "A. Multiple positional arguments",
            "B. Multiple keyword arguments",
            "C. Multiple loops",
            "D. Multiple classes"
        ],
        "answer": "B"
    },
    {
        "question": "Which module is commonly used for random numbers?",
        "options": ["A. random", "B. math", "C. numbers", "D. choice"],
        "answer": "A"
    },
    {
        "question": "Which module is used for mathematical functions?",
        "options": ["A. mathematics", "B. math", "C. maths", "D. calculation"],
        "answer": "B"
    },
    {
        "question": "Which function opens a file?",
        "options": ["A. file()", "B. open()", "C. read()", "D. load()"],
        "answer": "B"
    },
    {
        "question": "Which mode opens a file for writing?",
        "options": ["A. r", "B. w", "C. x", "D. read"],
        "answer": "B"
    },
    {
        "question": "Which mode opens a file for appending?",
        "options": ["A. a", "B. append", "C. w", "D. add"],
        "answer": "A"
    },
    {
        "question": "What does with open() help with?",
        "options": [
            "A. Automatic file handling",
            "B. Creating classes",
            "C. Running loops",
            "D. Installing modules"
        ],
        "answer": "A"
    },
    {
        "question": "What does __name__ == '__main__' check?",
        "options": [
            "A. File size",
            "B. Whether the file is run directly",
            "C. Python version",
            "D. Module name"
        ],
        "answer": "B"
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["A. Set", "B. List", "C. Dictionary", "D. Tuple"],
        "answer": "C"
    },
    {
        "question": "Which keyword returns a value from a function?",
        "options": ["A. give", "B. return", "C. output", "D. send"],
        "answer": "B"
    },
    {
        "question": "What is recursion?",
        "options": [
            "A. Function calling itself",
            "B. Loop without condition",
            "C. Creating a class",
            "D. Importing a module"
        ],
        "answer": "A"
    },
    {
        "question": "Which method converts dictionary keys into a view?",
        "options": ["A. keys()", "B. getkeys()", "C. keylist()", "D. values()"],
        "answer": "A"
    },
    {
        "question": "Which method returns dictionary values?",
        "options": ["A. data()", "B. values()", "C. getvalues()", "D. items()"],
        "answer": "B"
    },
    {
        "question": "Which method returns key-value pairs?",
        "options": ["A. pairs()", "B. items()", "C. keyvalues()", "D. entries()"],
        "answer": "B"
    },
    {
        "question": "Which operator checks object identity?",
        "options": ["A. ==", "B. is", "C. equals", "D. same"],
        "answer": "B"
    },
    {
        "question": "Which keyword creates an iterator?",
        "options": ["A. iter", "B. iterator", "C. next", "D. loop"],
        "answer": "A"
    },
    {
        "question": "Which function gets the next item from an iterator?",
        "options": ["A. next()", "B. get()", "C. following()", "D. move()"],
        "answer": "A"
    },
    {
        "question": "Which exception occurs when dividing by zero?",
        "options": [
            "A. ValueError",
            "B. ZeroDivisionError",
            "C. TypeError",
            "D. ArithmeticError"
        ],
        "answer": "B"
    },
    {
        "question": "Which exception occurs when using an invalid type?",
        "options": [
            "A. TypeError",
            "B. ValueError",
            "C. NameError",
            "D. SyntaxError"
        ],
        "answer": "A"
    },
    {
        "question": "Which exception occurs for an undefined variable?",
        "options": [
            "A. ValueError",
            "B. NameError",
            "C. TypeError",
            "D. KeyError"
        ],
        "answer": "B"
    },
    {
        "question": "Which exception occurs when a dictionary key does not exist?",
        "options": [
            "A. KeyError",
            "B. IndexError",
            "C. NameError",
            "D. LookupError"
        ],
        "answer": "A"
    },
    {
        "question": "Which exception occurs when a list index is out of range?",
        "options": [
            "A. IndexError",
            "B. KeyError",
            "C. RangeError",
            "D. ListError"
        ],
        "answer": "A"
    },
    {
        "question": "What does enumerate() provide?",
        "options": [
            "A. Only values",
            "B. Index and value",
            "C. Only indexes",
            "D. Dictionary keys"
        ],
        "answer": "B"
    },
    {
        "question": "What does zip() do?",
        "options": [
            "A. Compresses files",
            "B. Combines iterables element-wise",
            "C. Sorts lists",
            "D. Deletes duplicates"
        ],
        "answer": "B"
    },
    {
        "question": "What is list comprehension?",
        "options": [
            "A. Short way to create lists",
            "B. List deletion",
            "C. List sorting",
            "D. List copying"
        ],
        "answer": "A"
    },
    {
        "question": "Which symbol creates a set?",
        "options": ["A. []", "B. {}", "C. ()", "D. <>"],
        "answer": "B"
    },
    {
        "question": "Which collection is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used when defining an asynchronous function?",
        "options": ["A. async", "B. await", "C. asynchronous", "D. parallel"],
        "answer": "A"
    },
    {
        "question": "Which keyword pauses an async function until a result is available?",
        "options": ["A. wait", "B. await", "C. pause", "D. yield"],
        "answer": "B"
    },
    {
        "question": "What is a module?",
        "options": [
            "A. A Python file containing code",
            "B. A loop",
            "C. A variable",
            "D. A data type"
        ],
        "answer": "A"
    },
    {
        "question": "What is a package?",
        "options": [
            "A. Collection of modules",
            "B. A variable",
            "C. A loop",
            "D. A function"
        ],
        "answer": "A"
    },
    {
        "question": "Which command installs Python packages?",
        "options": ["A. python install", "B. pip install", "C. package add", "D. install pip"],
        "answer": "B"
    },
    {
        "question": "Which library is commonly used for HTTP requests?",
        "options": ["A. requests", "B. httpclient", "C. network", "D. web"],
        "answer": "A"
    },
    {
        "question": "Which module can work with JSON data?",
        "options": ["A. json", "B. data", "C. javascript", "D. object"],
        "answer": "A"
    },
    {
        "question": "Which function converts JSON text into Python objects?",
        "options": ["A. json.loads()", "B. json.loadtext()", "C. json.parse()", "D. json.convert()"],
        "answer": "A"
    },
    {
        "question": "Which function converts Python objects into JSON text?",
        "options": ["A. json.dumps()", "B. json.stringify()", "C. json.convert()", "D. json.text()"],
        "answer": "A"
    },
    {
        "question": "What is encapsulation?",
        "options": [
            "A. Bundling data and methods together",
            "B. Creating loops",
            "C. Importing modules",
            "D. Handling files"
        ],
        "answer": "A"
    },
    {
        "question": "What is polymorphism?",
        "options": [
            "A. Same interface with different implementations",
            "B. Multiple variables",
            "C. Multiple files",
            "D. Multiple loops"
        ],
        "answer": "A"
    },
    {
        "question": "What is abstraction?",
        "options": [
            "A. Hiding implementation details",
            "B. Hiding variables",
            "C. Removing code",
            "D. Creating objects"
        ],
        "answer": "A"
    },
    {
        "question": "Which decorator is commonly used for static methods?",
        "options": [
            "A. @static",
            "B. @staticmethod",
            "C. @staticmethods",
            "D. @method"
        ],
        "answer": "B"
    },
    {
        "question": "Which decorator creates a class method?",
        "options": [
            "A. @classmethod",
            "B. @class",
            "C. @method",
            "D. @classmethods"
        ],
        "answer": "A"
    },
    {
        "question": "What does isinstance() check?",
        "options": [
            "A. Object type/class relationship",
            "B. Variable length",
            "C. File size",
            "D. String length"
        ],
        "answer": "A"
    },
    {
        "question": "Which built-in function returns an absolute value?",
        "options": ["A. absolute()", "B. abs()", "C. positive()", "D. value()"],
        "answer": "B"
    },
    {
        "question": "Which built-in function rounds a number?",
        "options": ["A. round()", "B. rounded()", "C. approx()", "D. decimal()"],
        "answer": "A"
    }
]


# =========================
# SELECT LEVEL
# =========================

print("=" * 45)
print("              PYTHON QUIZ")
print("=" * 45)

print("\nSelect your level:")
print("1. Beginner      - 10 Questions")
print("2. Intermediate  - 25 Questions")
print("3. Advanced      - 50 Questions")

level = input("\nEnter your choice: ")


# =========================
# SELECT QUESTIONS
# =========================

if level == "1":

    questions = beginner
    level_name = "Beginner"

elif level == "2":

    questions = intermediate
    level_name = "Intermediate"

elif level == "3":

    questions = advanced
    level_name = "Advanced"

else:

    print("Invalid choice.")
    exit()


# Shuffle questions
random.shuffle(questions)


# =========================
# QUIZ
# =========================

score = 0

print("\n" + "=" * 45)
print(level_name, "LEVEL")
print("Questions:", len(questions))
print("=" * 45)


for number, question in enumerate(questions, start=1):

    print("\nQuestion", number)
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == question["answer"]:

        print("Correct!")
        score += 1

    else:

        print("Wrong!")
        print("Correct answer:", question["answer"])


# =========================
# RESULT
# =========================

total = len(questions)
percentage = (score / total) * 100


print("\n" + "=" * 45)
print("                 RESULT")
print("=" * 45)

print("Level      :", level_name)
print("Questions  :", total)
print("Correct    :", score)
print("Wrong      :", total - score)
print("Percentage :", round(percentage, 2), "%")


if percentage >= 90:
    grade = "Excellent"

elif percentage >= 75:
    grade = "Very Good"

elif percentage >= 60:
    grade = "Good"

elif percentage >= 40:
    grade = "Needs Improvement"

else:
    grade = "Keep Practicing"


print("Grade      :", grade)

print("=" * 45)
print("Quiz completed.")
print("=" * 45)
