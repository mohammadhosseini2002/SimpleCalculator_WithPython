#Create Simple Calculator With Python

User_Operator = input("Enter your Operator (+, -, *, /) --> ")

#if for Plus
if User_Operator == "+":
    Plus_First_Number = int(input("Enter your First Number (Plus +) --> "))
    Plus_Second_Number = int(input("Enter your Second Number (Plus +) --> "))
    Plus_SUM = Plus_First_Number + Plus_Second_Number
    print("Plus Result --> " , Plus_SUM)

if User_Operator == "-":
    Minus_First_Number = int(input("Enter your First Number (Minus -) --> "))
    Minus_Second_Number = int(input("Enter your Second Number (Minus -) --> "))
    Minus_SUM = Minus_First_Number - Minus_Second_Number
    print("Minus Result --> " , Minus_SUM)

if User_Operator == "*":
    Multiplication_First_Number = int(input("Enter your First Number (Multiplication *) --> "))
    Multiplication_Second_Number = int(input("Enter your Second Number (Multiplication *) --> "))
    Multiplication_SUM = Multiplication_First_Number * Multiplication_Second_Number
    print("Multiplication Result --> " , Multiplication_SUM)

if User_Operator == "/":
    Division_First_Number = int(input("Enter your First Number (Division /) --> "))
    Division_Second_Number = int(input("Enter your Second Number (Division /) --> "))
    Division_SUM = Division_First_Number / Division_Second_Number
    print("Division Result --> " , Division_SUM)